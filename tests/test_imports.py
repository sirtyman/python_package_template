"""Test for imports."""
import os


def test_import_modules():
    """Test packages and modules import."""
    for root, _, files in os.walk('../python_package_template'):
        package_name = root.split('/')[-1]

        for file in files:
            if file == "__init__.py":
                __import__(package_name)
                continue

            if file.endswith(".py"):
                module_name = file.split(".")[0]
                __import__(f"{package_name}.{module_name}")
