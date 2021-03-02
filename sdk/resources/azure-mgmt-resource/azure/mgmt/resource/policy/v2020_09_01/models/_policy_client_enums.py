# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class AliasPatternType(str, Enum):

    not_specified = "NotSpecified"  #: NotSpecified is not allowed.
    extract = "Extract"  #: Extract is the only allowed value.


class AliasPathTokenType(str, Enum):

    not_specified = "NotSpecified"  #: The token type is not specified.
    any = "Any"  #: The token type can be anything.
    string = "String"  #: The token type is string.
    object_enum = "Object"  #: The token type is object.
    array = "Array"  #: The token type is array.
    integer = "Integer"  #: The token type is integer.
    number = "Number"  #: The token type is number.
    boolean = "Boolean"  #: The token type is boolean.


class AliasPathAttributes(str, Enum):

    none = "None"  #: The token that the alias path is referring to has no attributes.
    modifiable = "Modifiable"  #: The token that the alias path is referring to is modifiable by policies with 'modify' effect.


class AliasType(str, Enum):

    not_specified = "NotSpecified"  #: Alias type is unknown (same as not providing alias type).
    plain_text = "PlainText"  #: Alias value is not secret.
    mask = "Mask"  #: Alias value is secret.


class EnforcementMode(str, Enum):

    default = "Default"  #: The policy effect is enforced during resource creation or update.
    do_not_enforce = "DoNotEnforce"  #: The policy effect is not enforced during resource creation or update.


class ResourceIdentityType(str, Enum):

    system_assigned = "SystemAssigned"  #: Indicates that a system assigned identity is associated with the resource.
    none = "None"  #: Indicates that no identity is associated with the resource or that the existing identity should be removed.


class PolicyType(str, Enum):

    not_specified = "NotSpecified"
    built_in = "BuiltIn"
    custom = "Custom"
    static = "Static"


class ParameterType(str, Enum):

    string = "String"
    array = "Array"
    object_enum = "Object"
    boolean = "Boolean"
    integer = "Integer"
    float_enum = "Float"
    date_time_enum = "DateTime"


class ExemptionCategory(str, Enum):

    waiver = "Waiver"  #: This category of exemptions usually means the scope is not applicable for the policy.
    mitigated = "Mitigated"  #: This category of exemptions usually means the mitigation actions have been applied to the scope.


class CreatedByType(str, Enum):

    user = "User"
    application = "Application"
    managed_identity = "ManagedIdentity"
    key = "Key"
