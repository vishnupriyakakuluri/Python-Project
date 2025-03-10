# #pytest
# Markers and Tags: Organizing and filtering tests
# In pytest, markers and tags are used to organize and filter tests in a more structured way.
# You can use markers to label tests based on their category or purpose. For example, you can mark tests as smoke, regression, or integration.
#
# import pytest
#
# @pytest.mark.smoke
# def test_login():
#     assert login("user", "password") == "success"
#
# @pytest.mark.regression
# def test_checkout():
#     assert checkout(cart) == "checkout successful"
#
# @pytest.mark.integration
# def test_payment_gateway():
#     assert process_payment(100) == "payment successful"
# ------------
# in terminal:
# pytest -m smoke
# or
# pytest -m "smoke and regression"
#
# ----------------
# .....................
# Custom Markers for Tagging Tests:
# You can define your own custom markers to help with test categorization. For example, if you want to mark tests as slow or fast, you can do it like this:
#
# import pytest
# @pytest.mark.slow
# def test_large_file_processing():
#     assert process_large_file() == "processed"
#
# @pytest.mark.fast
# def test_small_file_processing():
#     assert process_small_file() == "processed"
# ------------------------
# pytest -m slow
# pytest -m fast
# ......................................
# #Skipping Tests with a Marker
#
# import pytest
# import sys
# @pytest.mark.skipif(sys.platform == "win32", reason="does not run on Windows")
# def test_database_connection():
#     assert connect_to_database() == "connection successful"
# ..............................
# #Using pytest.ini to Define Markers
# To avoid warnings when using custom markers, you can define them in a pytest.ini configuration file:
# # pytest.ini
# [pytest]
# markers =
#     smoke: Run smoke tests
#     regression: Run regression tests
#     integration: Run integration tests
#     slow: Mark test as slow
#     fast: Mark test as fast
#
#
