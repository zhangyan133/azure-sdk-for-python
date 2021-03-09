# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._monitor_client_enums import *


class ActionGroupList(msrest.serialization.Model):
    """A list of action groups.

    :param value: The list of action groups.
    :type value: list[~$(python-base-namespace).v2018_09_01.models.ActionGroupResource]
    :param next_link: Provides the link to retrieve the next set of elements.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ActionGroupResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ActionGroupResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ActionGroupList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ActionGroupPatchBody(msrest.serialization.Model):
    """An action group object for the body of patch operations.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param enabled: Indicates whether this action group is enabled. If an action group is not
     enabled, then none of its actions will be activated.
    :type enabled: bool
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        enabled: Optional[bool] = True,
        **kwargs
    ):
        super(ActionGroupPatchBody, self).__init__(**kwargs)
        self.tags = tags
        self.enabled = enabled


class Resource(msrest.serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class ActionGroupResource(Resource):
    """An action group resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param group_short_name: The short name of the action group. This will be used in SMS messages.
    :type group_short_name: str
    :param enabled: Indicates whether this action group is enabled. If an action group is not
     enabled, then none of its receivers will receive communications.
    :type enabled: bool
    :param email_receivers: The list of email receivers that are part of this action group.
    :type email_receivers: list[~$(python-base-namespace).v2018_09_01.models.EmailReceiver]
    :param sms_receivers: The list of SMS receivers that are part of this action group.
    :type sms_receivers: list[~$(python-base-namespace).v2018_09_01.models.SmsReceiver]
    :param webhook_receivers: The list of webhook receivers that are part of this action group.
    :type webhook_receivers: list[~$(python-base-namespace).v2018_09_01.models.WebhookReceiver]
    :param itsm_receivers: The list of ITSM receivers that are part of this action group.
    :type itsm_receivers: list[~$(python-base-namespace).v2018_09_01.models.ItsmReceiver]
    :param azure_app_push_receivers: The list of AzureAppPush receivers that are part of this
     action group.
    :type azure_app_push_receivers: list[~$(python-base-
     namespace).v2018_09_01.models.AzureAppPushReceiver]
    :param automation_runbook_receivers: The list of AutomationRunbook receivers that are part of
     this action group.
    :type automation_runbook_receivers: list[~$(python-base-
     namespace).v2018_09_01.models.AutomationRunbookReceiver]
    :param voice_receivers: The list of voice receivers that are part of this action group.
    :type voice_receivers: list[~$(python-base-namespace).v2018_09_01.models.VoiceReceiver]
    :param logic_app_receivers: The list of logic app receivers that are part of this action group.
    :type logic_app_receivers: list[~$(python-base-namespace).v2018_09_01.models.LogicAppReceiver]
    :param azure_function_receivers: The list of azure function receivers that are part of this
     action group.
    :type azure_function_receivers: list[~$(python-base-
     namespace).v2018_09_01.models.AzureFunctionReceiver]
    :param arm_role_receivers: The list of ARM role receivers that are part of this action group.
     Roles are Azure RBAC roles and only built-in roles are supported.
    :type arm_role_receivers: list[~$(python-base-namespace).v2018_09_01.models.ArmRoleReceiver]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'group_short_name': {'max_length': 12, 'min_length': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'group_short_name': {'key': 'properties.groupShortName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'email_receivers': {'key': 'properties.emailReceivers', 'type': '[EmailReceiver]'},
        'sms_receivers': {'key': 'properties.smsReceivers', 'type': '[SmsReceiver]'},
        'webhook_receivers': {'key': 'properties.webhookReceivers', 'type': '[WebhookReceiver]'},
        'itsm_receivers': {'key': 'properties.itsmReceivers', 'type': '[ItsmReceiver]'},
        'azure_app_push_receivers': {'key': 'properties.azureAppPushReceivers', 'type': '[AzureAppPushReceiver]'},
        'automation_runbook_receivers': {'key': 'properties.automationRunbookReceivers', 'type': '[AutomationRunbookReceiver]'},
        'voice_receivers': {'key': 'properties.voiceReceivers', 'type': '[VoiceReceiver]'},
        'logic_app_receivers': {'key': 'properties.logicAppReceivers', 'type': '[LogicAppReceiver]'},
        'azure_function_receivers': {'key': 'properties.azureFunctionReceivers', 'type': '[AzureFunctionReceiver]'},
        'arm_role_receivers': {'key': 'properties.armRoleReceivers', 'type': '[ArmRoleReceiver]'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        group_short_name: Optional[str] = None,
        enabled: Optional[bool] = True,
        email_receivers: Optional[List["EmailReceiver"]] = None,
        sms_receivers: Optional[List["SmsReceiver"]] = None,
        webhook_receivers: Optional[List["WebhookReceiver"]] = None,
        itsm_receivers: Optional[List["ItsmReceiver"]] = None,
        azure_app_push_receivers: Optional[List["AzureAppPushReceiver"]] = None,
        automation_runbook_receivers: Optional[List["AutomationRunbookReceiver"]] = None,
        voice_receivers: Optional[List["VoiceReceiver"]] = None,
        logic_app_receivers: Optional[List["LogicAppReceiver"]] = None,
        azure_function_receivers: Optional[List["AzureFunctionReceiver"]] = None,
        arm_role_receivers: Optional[List["ArmRoleReceiver"]] = None,
        **kwargs
    ):
        super(ActionGroupResource, self).__init__(location=location, tags=tags, **kwargs)
        self.group_short_name = group_short_name
        self.enabled = enabled
        self.email_receivers = email_receivers
        self.sms_receivers = sms_receivers
        self.webhook_receivers = webhook_receivers
        self.itsm_receivers = itsm_receivers
        self.azure_app_push_receivers = azure_app_push_receivers
        self.automation_runbook_receivers = automation_runbook_receivers
        self.voice_receivers = voice_receivers
        self.logic_app_receivers = logic_app_receivers
        self.azure_function_receivers = azure_function_receivers
        self.arm_role_receivers = arm_role_receivers


class ArmRoleReceiver(msrest.serialization.Model):
    """An arm role receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the arm role receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param role_id: Required. The arm role id.
    :type role_id: str
    """

    _validation = {
        'name': {'required': True},
        'role_id': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'role_id': {'key': 'roleId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        role_id: str,
        **kwargs
    ):
        super(ArmRoleReceiver, self).__init__(**kwargs)
        self.name = name
        self.role_id = role_id


class AutomationRunbookReceiver(msrest.serialization.Model):
    """The Azure Automation Runbook notification receiver.

    All required parameters must be populated in order to send to Azure.

    :param automation_account_id: Required. The Azure automation account Id which holds this
     runbook and authenticate to Azure resource.
    :type automation_account_id: str
    :param runbook_name: Required. The name for this runbook.
    :type runbook_name: str
    :param webhook_resource_id: Required. The resource id for webhook linked to this runbook.
    :type webhook_resource_id: str
    :param is_global_runbook: Required. Indicates whether this instance is global runbook.
    :type is_global_runbook: bool
    :param name: Indicates name of the webhook.
    :type name: str
    :param service_uri: The URI where webhooks should be sent.
    :type service_uri: str
    """

    _validation = {
        'automation_account_id': {'required': True},
        'runbook_name': {'required': True},
        'webhook_resource_id': {'required': True},
        'is_global_runbook': {'required': True},
    }

    _attribute_map = {
        'automation_account_id': {'key': 'automationAccountId', 'type': 'str'},
        'runbook_name': {'key': 'runbookName', 'type': 'str'},
        'webhook_resource_id': {'key': 'webhookResourceId', 'type': 'str'},
        'is_global_runbook': {'key': 'isGlobalRunbook', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        automation_account_id: str,
        runbook_name: str,
        webhook_resource_id: str,
        is_global_runbook: bool,
        name: Optional[str] = None,
        service_uri: Optional[str] = None,
        **kwargs
    ):
        super(AutomationRunbookReceiver, self).__init__(**kwargs)
        self.automation_account_id = automation_account_id
        self.runbook_name = runbook_name
        self.webhook_resource_id = webhook_resource_id
        self.is_global_runbook = is_global_runbook
        self.name = name
        self.service_uri = service_uri


class AzureAppPushReceiver(msrest.serialization.Model):
    """The Azure mobile App push notification receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the Azure mobile app push receiver. Names must be unique
     across all receivers within an action group.
    :type name: str
    :param email_address: Required. The email address registered for the Azure mobile app.
    :type email_address: str
    """

    _validation = {
        'name': {'required': True},
        'email_address': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        email_address: str,
        **kwargs
    ):
        super(AzureAppPushReceiver, self).__init__(**kwargs)
        self.name = name
        self.email_address = email_address


class AzureFunctionReceiver(msrest.serialization.Model):
    """An azure function receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the azure function receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param function_app_resource_id: Required. The azure resource id of the function app.
    :type function_app_resource_id: str
    :param function_name: Required. The function name in the function app.
    :type function_name: str
    :param http_trigger_url: Required. The http trigger url where http request sent to.
    :type http_trigger_url: str
    """

    _validation = {
        'name': {'required': True},
        'function_app_resource_id': {'required': True},
        'function_name': {'required': True},
        'http_trigger_url': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'function_app_resource_id': {'key': 'functionAppResourceId', 'type': 'str'},
        'function_name': {'key': 'functionName', 'type': 'str'},
        'http_trigger_url': {'key': 'httpTriggerUrl', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        function_app_resource_id: str,
        function_name: str,
        http_trigger_url: str,
        **kwargs
    ):
        super(AzureFunctionReceiver, self).__init__(**kwargs)
        self.name = name
        self.function_app_resource_id = function_app_resource_id
        self.function_name = function_name
        self.http_trigger_url = http_trigger_url


class Baseline(msrest.serialization.Model):
    """The baseline values for a single sensitivity value.

    All required parameters must be populated in order to send to Azure.

    :param sensitivity: Required. The sensitivity of the baseline. Possible values include: "Low",
     "Medium", "High".
    :type sensitivity: str or ~$(python-base-namespace).v2018_09_01.models.Sensitivity
    :param low_thresholds: Required. The low thresholds of the baseline.
    :type low_thresholds: list[float]
    :param high_thresholds: Required. The high thresholds of the baseline.
    :type high_thresholds: list[float]
    :param timestamps: the array of timestamps of the baselines.
    :type timestamps: list[~datetime.datetime]
    :param prediction_result_type: The prediction result type of the baseline. Possible values
     include: 0, 1, 2.
    :type prediction_result_type: str or ~$(python-base-
     namespace).v2018_09_01.models.PredictionResultType
    :param error_type: The error type of the baseline. Possible values include: 0, 1, 2, 3, 4, 100,
     200.
    :type error_type: str or ~$(python-base-namespace).v2018_09_01.models.ErrorType
    """

    _validation = {
        'sensitivity': {'required': True},
        'low_thresholds': {'required': True},
        'high_thresholds': {'required': True},
    }

    _attribute_map = {
        'sensitivity': {'key': 'sensitivity', 'type': 'str'},
        'low_thresholds': {'key': 'lowThresholds', 'type': '[float]'},
        'high_thresholds': {'key': 'highThresholds', 'type': '[float]'},
        'timestamps': {'key': 'timestamps', 'type': '[iso-8601]'},
        'prediction_result_type': {'key': 'PredictionResultType', 'type': 'int'},
        'error_type': {'key': 'ErrorType', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        sensitivity: Union[str, "Sensitivity"],
        low_thresholds: List[float],
        high_thresholds: List[float],
        timestamps: Optional[List[datetime.datetime]] = None,
        prediction_result_type: Optional[Union[int, "PredictionResultType"]] = None,
        error_type: Optional[Union[int, "ErrorType"]] = None,
        **kwargs
    ):
        super(Baseline, self).__init__(**kwargs)
        self.sensitivity = sensitivity
        self.low_thresholds = low_thresholds
        self.high_thresholds = high_thresholds
        self.timestamps = timestamps
        self.prediction_result_type = prediction_result_type
        self.error_type = error_type


class BaselineMetadataValue(msrest.serialization.Model):
    """Represents a baseline metadata value.

    :param name: The name of the metadata.
    :type name: ~$(python-base-namespace).v2018_09_01.models.LocalizableString
    :param value: The value of the metadata.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional["LocalizableString"] = None,
        value: Optional[str] = None,
        **kwargs
    ):
        super(BaselineMetadataValue, self).__init__(**kwargs)
        self.name = name
        self.value = value


class BaselineResponse(msrest.serialization.Model):
    """The response to a baseline query.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The metric baseline ID.
    :vartype id: str
    :ivar type: The resource type of the baseline resource.
    :vartype type: str
    :ivar name: The name and the display name of the metric, i.e. it is localizable string.
    :vartype name: ~$(python-base-namespace).v2018_09_01.models.LocalizableString
    :param timestamps: The array of timestamps of the baselines.
    :type timestamps: list[~datetime.datetime]
    :param baseline: The baseline values for each sensitivity.
    :type baseline: list[~$(python-base-namespace).v2018_09_01.models.Baseline]
    :param metdata: The baseline metadata values.
    :type metdata: list[~$(python-base-namespace).v2018_09_01.models.BaselineMetadataValue]
    :param prediction_result_type: The prediction result type of the baseline. Possible values
     include: 0, 1, 2.
    :type prediction_result_type: str or ~$(python-base-
     namespace).v2018_09_01.models.PredictionResultType
    :param error_type: The error type of the baseline. Possible values include: 0, 1, 2, 3, 4, 100,
     200.
    :type error_type: str or ~$(python-base-namespace).v2018_09_01.models.ErrorType
    :param timespan: The timespan for which the data was retrieved. Its value consists of two
     datetimes concatenated, separated by '/'.  This may be adjusted in the future and returned back
     from what was originally requested.
    :type timespan: str
    :param interval: The interval (window size) for which the metric data was returned in.  This
     may be adjusted in the future and returned back from what was originally requested.  This is
     not present if a metadata request was made.
    :type interval: ~datetime.timedelta
    :param aggregation: The aggregation type of the metric.
    :type aggregation: str
    :ivar internal_operation_id: internal operation id.
    :vartype internal_operation_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'internal_operation_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'timestamps': {'key': 'timestamps', 'type': '[iso-8601]'},
        'baseline': {'key': 'baseline', 'type': '[Baseline]'},
        'metdata': {'key': 'metdata', 'type': '[BaselineMetadataValue]'},
        'prediction_result_type': {'key': 'predictionResultType', 'type': 'int'},
        'error_type': {'key': 'errorType', 'type': 'int'},
        'timespan': {'key': 'properties.timespan', 'type': 'str'},
        'interval': {'key': 'properties.interval', 'type': 'duration'},
        'aggregation': {'key': 'properties.aggregation', 'type': 'str'},
        'internal_operation_id': {'key': 'properties.internalOperationId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        timestamps: Optional[List[datetime.datetime]] = None,
        baseline: Optional[List["Baseline"]] = None,
        metdata: Optional[List["BaselineMetadataValue"]] = None,
        prediction_result_type: Optional[Union[int, "PredictionResultType"]] = None,
        error_type: Optional[Union[int, "ErrorType"]] = None,
        timespan: Optional[str] = None,
        interval: Optional[datetime.timedelta] = None,
        aggregation: Optional[str] = None,
        **kwargs
    ):
        super(BaselineResponse, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.timestamps = timestamps
        self.baseline = baseline
        self.metdata = metdata
        self.prediction_result_type = prediction_result_type
        self.error_type = error_type
        self.timespan = timespan
        self.interval = interval
        self.aggregation = aggregation
        self.internal_operation_id = None


class CalculateBaselineResponse(msrest.serialization.Model):
    """The response to a calculate baseline call.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The resource type of the baseline resource.
    :type type: str
    :param timestamps: The array of timestamps of the baselines.
    :type timestamps: list[~datetime.datetime]
    :param baseline: Required. The baseline values for each sensitivity.
    :type baseline: list[~$(python-base-namespace).v2018_09_01.models.Baseline]
    :param statistics: The statistics.
    :type statistics: ~$(python-base-
     namespace).v2018_09_01.models.CalculateBaselineResponseStatistics
    :ivar internal_operation_id: internal operation id.
    :vartype internal_operation_id: str
    :param error_type: The error type for calculating the baseline. Possible values include: 0, 1,
     2, 3, 4, 100, 200.
    :type error_type: str or ~$(python-base-namespace).v2018_09_01.models.ErrorTypeAutoGenerated
    """

    _validation = {
        'type': {'required': True},
        'baseline': {'required': True},
        'internal_operation_id': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'timestamps': {'key': 'timestamps', 'type': '[iso-8601]'},
        'baseline': {'key': 'baseline', 'type': '[Baseline]'},
        'statistics': {'key': 'statistics', 'type': 'CalculateBaselineResponseStatistics'},
        'internal_operation_id': {'key': 'internalOperationId', 'type': 'str'},
        'error_type': {'key': 'errorType', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        type: str,
        baseline: List["Baseline"],
        timestamps: Optional[List[datetime.datetime]] = None,
        statistics: Optional["CalculateBaselineResponseStatistics"] = None,
        error_type: Optional[Union[int, "ErrorTypeAutoGenerated"]] = None,
        **kwargs
    ):
        super(CalculateBaselineResponse, self).__init__(**kwargs)
        self.type = type
        self.timestamps = timestamps
        self.baseline = baseline
        self.statistics = statistics
        self.internal_operation_id = None
        self.error_type = error_type


class CalculateBaselineResponseStatistics(msrest.serialization.Model):
    """The statistics.

    :param is_eligible: is series eligible for dynamic threshold analysis.
    :type is_eligible: bool
    :param status: The list of extended status for calculating the baseline.
    :type status: list[str]
    :param seasonality_period: The seasonality period for calculating the baseline.
    :type seasonality_period: int
    """

    _attribute_map = {
        'is_eligible': {'key': 'isEligible', 'type': 'bool'},
        'status': {'key': 'status', 'type': '[str]'},
        'seasonality_period': {'key': 'seasonalityPeriod', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        is_eligible: Optional[bool] = None,
        status: Optional[List[str]] = None,
        seasonality_period: Optional[int] = None,
        **kwargs
    ):
        super(CalculateBaselineResponseStatistics, self).__init__(**kwargs)
        self.is_eligible = is_eligible
        self.status = status
        self.seasonality_period = seasonality_period


class EmailReceiver(msrest.serialization.Model):
    """An email receiver.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the email receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param email_address: Required. The email address of this receiver.
    :type email_address: str
    :ivar status: The receiver status of the e-mail. Possible values include: "NotSpecified",
     "Enabled", "Disabled".
    :vartype status: str or ~$(python-base-namespace).v2018_09_01.models.ReceiverStatus
    """

    _validation = {
        'name': {'required': True},
        'email_address': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        email_address: str,
        **kwargs
    ):
        super(EmailReceiver, self).__init__(**kwargs)
        self.name = name
        self.email_address = email_address
        self.status = None


class EnableRequest(msrest.serialization.Model):
    """Describes a receiver that should be resubscribed.

    All required parameters must be populated in order to send to Azure.

    :param receiver_name: Required. The name of the receiver to resubscribe.
    :type receiver_name: str
    """

    _validation = {
        'receiver_name': {'required': True},
    }

    _attribute_map = {
        'receiver_name': {'key': 'receiverName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        receiver_name: str,
        **kwargs
    ):
        super(EnableRequest, self).__init__(**kwargs)
        self.receiver_name = receiver_name


class ErrorResponse(msrest.serialization.Model):
    """Describes the format of Error response.

    :param code: Error code.
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ItsmReceiver(msrest.serialization.Model):
    """An Itsm receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the Itsm receiver. Names must be unique across all receivers
     within an action group.
    :type name: str
    :param workspace_id: Required. OMS LA instance identifier.
    :type workspace_id: str
    :param connection_id: Required. Unique identification of ITSM connection among multiple defined
     in above workspace.
    :type connection_id: str
    :param ticket_configuration: Required. JSON blob for the configurations of the ITSM action.
     CreateMultipleWorkItems option will be part of this blob as well.
    :type ticket_configuration: str
    :param region: Required. Region in which workspace resides. Supported
     values:'centralindia','japaneast','southeastasia','australiasoutheast','uksouth','westcentralus','canadacentral','eastus','westeurope'.
    :type region: str
    """

    _validation = {
        'name': {'required': True},
        'workspace_id': {'required': True},
        'connection_id': {'required': True},
        'ticket_configuration': {'required': True},
        'region': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'workspace_id': {'key': 'workspaceId', 'type': 'str'},
        'connection_id': {'key': 'connectionId', 'type': 'str'},
        'ticket_configuration': {'key': 'ticketConfiguration', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        workspace_id: str,
        connection_id: str,
        ticket_configuration: str,
        region: str,
        **kwargs
    ):
        super(ItsmReceiver, self).__init__(**kwargs)
        self.name = name
        self.workspace_id = workspace_id
        self.connection_id = connection_id
        self.ticket_configuration = ticket_configuration
        self.region = region


class LocalizableString(msrest.serialization.Model):
    """The localizable string class.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. The invariant value.
    :type value: str
    :param localized_value: The locale specific value.
    :type localized_value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: str,
        localized_value: Optional[str] = None,
        **kwargs
    ):
        super(LocalizableString, self).__init__(**kwargs)
        self.value = value
        self.localized_value = localized_value


class LogicAppReceiver(msrest.serialization.Model):
    """A logic app receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the logic app receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param resource_id: Required. The azure resource id of the logic app receiver.
    :type resource_id: str
    :param callback_url: Required. The callback url where http request sent to.
    :type callback_url: str
    """

    _validation = {
        'name': {'required': True},
        'resource_id': {'required': True},
        'callback_url': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'callback_url': {'key': 'callbackUrl', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        resource_id: str,
        callback_url: str,
        **kwargs
    ):
        super(LogicAppReceiver, self).__init__(**kwargs)
        self.name = name
        self.resource_id = resource_id
        self.callback_url = callback_url


class SmsReceiver(msrest.serialization.Model):
    """An SMS receiver.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SMS receiver. Names must be unique across all receivers
     within an action group.
    :type name: str
    :param country_code: Required. The country code of the SMS receiver.
    :type country_code: str
    :param phone_number: Required. The phone number of the SMS receiver.
    :type phone_number: str
    :ivar status: The status of the receiver. Possible values include: "NotSpecified", "Enabled",
     "Disabled".
    :vartype status: str or ~$(python-base-namespace).v2018_09_01.models.ReceiverStatus
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
        'phone_number': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        country_code: str,
        phone_number: str,
        **kwargs
    ):
        super(SmsReceiver, self).__init__(**kwargs)
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number
        self.status = None


class TimeSeriesInformation(msrest.serialization.Model):
    """The time series info needed for calculating the baseline.

    All required parameters must be populated in order to send to Azure.

    :param sensitivities: Required. The list of sensitivities for calculating the baseline.
    :type sensitivities: list[str]
    :param values: Required. The metric values to calculate the baseline.
    :type values: list[float]
    :param timestamps: The array of timestamps of the baselines.
    :type timestamps: list[~datetime.datetime]
    """

    _validation = {
        'sensitivities': {'required': True},
        'values': {'required': True},
    }

    _attribute_map = {
        'sensitivities': {'key': 'sensitivities', 'type': '[str]'},
        'values': {'key': 'values', 'type': '[float]'},
        'timestamps': {'key': 'timestamps', 'type': '[iso-8601]'},
    }

    def __init__(
        self,
        *,
        sensitivities: List[str],
        values: List[float],
        timestamps: Optional[List[datetime.datetime]] = None,
        **kwargs
    ):
        super(TimeSeriesInformation, self).__init__(**kwargs)
        self.sensitivities = sensitivities
        self.values = values
        self.timestamps = timestamps


class VoiceReceiver(msrest.serialization.Model):
    """A voice receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the voice receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param country_code: Required. The country code of the voice receiver.
    :type country_code: str
    :param phone_number: Required. The phone number of the voice receiver.
    :type phone_number: str
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
        'phone_number': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        country_code: str,
        phone_number: str,
        **kwargs
    ):
        super(VoiceReceiver, self).__init__(**kwargs)
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number


class WebhookReceiver(msrest.serialization.Model):
    """A webhook receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the webhook receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param service_uri: Required. The URI where webhooks should be sent.
    :type service_uri: str
    """

    _validation = {
        'name': {'required': True},
        'service_uri': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        service_uri: str,
        **kwargs
    ):
        super(WebhookReceiver, self).__init__(**kwargs)
        self.name = name
        self.service_uri = service_uri
