from django.db import models


# Create your models here.

# Data Model
class Dataset(models.Model):
    """dataset name is the name of table containing the data of the specific dataset"""
    dataset_name = models.CharField(null=False, default="", max_length=50)
    dataset_title = models.CharField(null=False, default="", max_length=50)
    dataset_description = models.TextField(null=False, default="")
    dataset_provider = models.CharField(null=False, default="", max_length=50)
    dataset_date_creation = models.DateTimeField(auto_now_add=True)
    dataset_date_update = models.DateTimeField(auto_now=True)
    dataset_django_model = models.CharField(null=False, default="", max_length=50)


class Variable(models.Model):
    var_name = models.CharField(null=False, default="", max_length=50)
    var_title = models.CharField(null=False, default="", max_length=50)
    var_category = models.CharField(null=False, default="", max_length=50)
    var_definition = models.TextField(null=False, default="")
    var_unit = models.CharField(null=False, default="", max_length=50)
    dataset_relation = models.ForeignKey(Dataset, null=False, on_delete=models.CASCADE)
    variable_table_name = models.CharField(null=True, max_length=50)


# Variable Tables
# If a variable does not correspond to an independent table then the dataset contains only its value
# If a variable corresponds to an independent table then the dataset contains the id of a specific record in the
# independent table
class TestVariable(models.Model):
    test_var_obj_name = models.CharField(null=False, default="", max_length=50)
    test_var_obj_title = models.CharField(null=False, default="", max_length=50)


# Datasets
class TestDataset(models.Model):
    test_var_1 = models.ForeignKey(TestVariable, on_delete=models.CASCADE)
    value = models.CharField(null=False, default="", max_length=50)
