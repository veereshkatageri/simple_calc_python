from conans import ConanFile, python_requires

import os
import sys
import shutil
import subprocess
import platform
from packaging import version

"""
Read document generation type (if passed locally or through jenkins build job)
If it is not set, use the default type i.e, upload_e2e
"""

docu_generation_type = os.environ.get('DOCU_GENERATION_TYPE')
if docu_generation_type is None:
    docu_generation_type = 'upload_e2e'

# standard attributes
var_name = "simple_calc_python"
var_version = "0.0.1"
var_description = "Source code documentation"

# customized attribute
# adjust var_parent_dir_config_file accordingly if it is not a single folder
var_parent_dir_config_file = 'Simple_Calculator'
var_folder_html = "SCD_Demo_Simple_Calculator_DocHtml"
var_folder_spelling = "SCD_Demo_Simple_Calculator_DocSpelling"

class ConanRecipe(ConanFile):
    name            = var_name
    version         = var_version
    generators      = "txt"
    description     = var_description
    settings        = "os", "arch"
    scm             = { "type": "git", "url": "auto", "revision": "auto" }
    no_copy_source  = True
    options = {}
    default_options = {}

    # Set version in configuration file conf.py
    os.environ["version"] = version

    def build_requirements(self):
        command = subprocess.check_output(['sphinx-build', '--version']).decode("utf8")
        if not (version.parse(command.strip()) == version.parse("sphinx-build 2.4.4") or
                version.parse(command.strip()) > version.parse("sphinx-build 2.4.4")):
            self.output.error("Sphinx Requirements are not satisfied")
            exit(1)

    def requirements(self):
        pass

    def build(self):
        # self.source_folder and self.build_folder are different in conan build method
        # but there are same in conan create method

        input_folder = None
        configuration_file = os.path.join(self.source_folder, var_parent_dir_config_file, 'conf.py')

        output_folder = os.path.join(self.build_folder, 'package', var_folder_html)
        os.makedirs(output_folder, exist_ok=True)

        # Adjust the parent folder of config file path for both conan build and conan create method
        if os.path.exists(configuration_file):
            input_folder = os.path.join(self.source_folder, var_parent_dir_config_file)
        else:
            input_folder = self.source_folder

        # -- target build html ----------------------------------------
        try:
            command = subprocess.run(['sphinx-build', '-b', 'html', input_folder, output_folder],
                                     check=True)

            # make archieve
            shutil.make_archive(var_folder_html, 'zip', output_folder)
        except subprocess.CalledProcessError as err:
            print(err.output)

        # -- target build spelling ----------------------------------------
        output_folder = os.path.join(self.build_folder, 'package', var_folder_spelling)
        os.makedirs(output_folder, exist_ok=True)


        try:
            command = subprocess.run(['sphinx-build', '-b', 'spelling', input_folder, output_folder],
                                     check=True)
            output_folder = os.path.join(self.build_folder, 'package', var_folder_spelling)
            os.makedirs(output_folder, exist_ok=True)
            # make archieve
            shutil.make_archive(var_folder_spelling, 'zip', output_folder)
        except subprocess.CalledProcessError as err:
            print(err.output)

