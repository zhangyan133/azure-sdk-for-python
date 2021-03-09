# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ActionGroupList(msrest.serialization.Model):
    """A list of action groups.

    :param value: The list of action groups.
    :type value: list[~$(python-base-namespace).v2019_03_01.models.ActionGroupResource]
    :param next_link: Provides the link to retrieve the next set of elements.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ActionGroupResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ActionGroupList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


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
        **kwargs
    ):
        super(ActionGroupPatchBody, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.enabled = kwargs.get('enabled', True)


class AzureResource(msrest.serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar kind: Azure resource kind.
    :vartype kind: str
    :ivar identity: Azure resource identity.
    :vartype identity: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'readonly': True},
        'identity': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AzureResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.kind = None
        self.identity = None
        self.location = kwargs['location']
        self.tags = kwargs.get('tags', None)


class ActionGroupResource(AzureResource):
    """An action group resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar kind: Azure resource kind.
    :vartype kind: str
    :ivar identity: Azure resource identity.
    :vartype identity: str
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
    :type email_receivers: list[~$(python-base-namespace).v2019_03_01.models.EmailReceiver]
    :param sms_receivers: The list of SMS receivers that are part of this action group.
    :type sms_receivers: list[~$(python-base-namespace).v2019_03_01.models.SmsReceiver]
    :param webhook_receivers: The list of webhook receivers that are part of this action group.
    :type webhook_receivers: list[~$(python-base-namespace).v2019_03_01.models.WebhookReceiver]
    :param itsm_receivers: The list of ITSM receivers that are part of this action group.
    :type itsm_receivers: list[~$(python-base-namespace).v2019_03_01.models.ItsmReceiver]
    :param azure_app_push_receivers: The list of AzureAppPush receivers that are part of this
     action group.
    :type azure_app_push_receivers: list[~$(python-base-
     namespace).v2019_03_01.models.AzureAppPushReceiver]
    :param automation_runbook_receivers: The list of AutomationRunbook receivers that are part of
     this action group.
    :type automation_runbook_receivers: list[~$(python-base-
     namespace).v2019_03_01.models.AutomationRunbookReceiver]
    :param voice_receivers: The list of voice receivers that are part of this action group.
    :type voice_receivers: list[~$(python-base-namespace).v2019_03_01.models.VoiceReceiver]
    :param logic_app_receivers: The list of logic app receivers that are part of this action group.
    :type logic_app_receivers: list[~$(python-base-namespace).v2019_03_01.models.LogicAppReceiver]
    :param azure_function_receivers: The list of azure function receivers that are part of this
     action group.
    :type azure_function_receivers: list[~$(python-base-
     namespace).v2019_03_01.models.AzureFunctionReceiver]
    :param arm_role_receivers: The list of ARM role receivers that are part of this action group.
     Roles are Azure RBAC roles and only built-in roles are supported.
    :type arm_role_receivers: list[~$(python-base-namespace).v2019_03_01.models.ArmRoleReceiver]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'readonly': True},
        'identity': {'readonly': True},
        'location': {'required': True},
        'group_short_name': {'max_length': 12, 'min_length': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'str'},
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
        **kwargs
    ):
        super(ActionGroupResource, self).__init__(**kwargs)
        self.group_short_name = kwargs.get('group_short_name', None)
        self.enabled = kwargs.get('enabled', True)
        self.email_receivers = kwargs.get('email_receivers', None)
        self.sms_receivers = kwargs.get('sms_receivers', None)
        self.webhook_receivers = kwargs.get('webhook_receivers', None)
        self.itsm_receivers = kwargs.get('itsm_receivers', None)
        self.azure_app_push_receivers = kwargs.get('azure_app_push_receivers', None)
        self.automation_runbook_receivers = kwargs.get('automation_runbook_receivers', None)
        self.voice_receivers = kwargs.get('voice_receivers', None)
        self.logic_app_receivers = kwargs.get('logic_app_receivers', None)
        self.azure_function_receivers = kwargs.get('azure_function_receivers', None)
        self.arm_role_receivers = kwargs.get('arm_role_receivers', None)


class ArmRoleReceiver(msrest.serialization.Model):
    """An arm role receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the arm role receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param role_id: Required. The arm role id.
    :type role_id: str
    :param use_common_alert_schema: Required. Indicates whether to use common alert schema.
    :type use_common_alert_schema: bool
    """

    _validation = {
        'name': {'required': True},
        'role_id': {'required': True},
        'use_common_alert_schema': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'role_id': {'key': 'roleId', 'type': 'str'},
        'use_common_alert_schema': {'key': 'useCommonAlertSchema', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ArmRoleReceiver, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.role_id = kwargs['role_id']
        self.use_common_alert_schema = kwargs['use_common_alert_schema']


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
    :param use_common_alert_schema: Required. Indicates whether to use common alert schema.
    :type use_common_alert_schema: bool
    """

    _validation = {
        'automation_account_id': {'required': True},
        'runbook_name': {'required': True},
        'webhook_resource_id': {'required': True},
        'is_global_runbook': {'required': True},
        'use_common_alert_schema': {'required': True},
    }

    _attribute_map = {
        'automation_account_id': {'key': 'automationAccountId', 'type': 'str'},
        'runbook_name': {'key': 'runbookName', 'type': 'str'},
        'webhook_resource_id': {'key': 'webhookResourceId', 'type': 'str'},
        'is_global_runbook': {'key': 'isGlobalRunbook', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
        'use_common_alert_schema': {'key': 'useCommonAlertSchema', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AutomationRunbookReceiver, self).__init__(**kwargs)
        self.automation_account_id = kwargs['automation_account_id']
        self.runbook_name = kwargs['runbook_name']
        self.webhook_resource_id = kwargs['webhook_resource_id']
        self.is_global_runbook = kwargs['is_global_runbook']
        self.name = kwargs.get('name', None)
        self.service_uri = kwargs.get('service_uri', None)
        self.use_common_alert_schema = kwargs['use_common_alert_schema']


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
        **kwargs
    ):
        super(AzureAppPushReceiver, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.email_address = kwargs['email_address']


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
    :param use_common_alert_schema: Required. Indicates whether to use common alert schema.
    :type use_common_alert_schema: bool
    """

    _validation = {
        'name': {'required': True},
        'function_app_resource_id': {'required': True},
        'function_name': {'required': True},
        'http_trigger_url': {'required': True},
        'use_common_alert_schema': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'function_app_resource_id': {'key': 'functionAppResourceId', 'type': 'str'},
        'function_name': {'key': 'functionName', 'type': 'str'},
        'http_trigger_url': {'key': 'httpTriggerUrl', 'type': 'str'},
        'use_common_alert_schema': {'key': 'useCommonAlertSchema', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AzureFunctionReceiver, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.function_app_resource_id = kwargs['function_app_resource_id']
        self.function_name = kwargs['function_name']
        self.http_trigger_url = kwargs['http_trigger_url']
        self.use_common_alert_schema = kwargs['use_common_alert_schema']


class BaselineMetadata(msrest.serialization.Model):
    """Represents a baseline metadata value.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the baseline metadata.
    :type name: str
    :param value: Required. Value of the baseline metadata.
    :type value: str
    """

    _validation = {
        'name': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(BaselineMetadata, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.value = kwargs['value']


class EmailReceiver(msrest.serialization.Model):
    """An email receiver.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the email receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param email_address: Required. The email address of this receiver.
    :type email_address: str
    :param use_common_alert_schema: Required. Indicates whether to use common alert schema.
    :type use_common_alert_schema: bool
    :ivar status: The receiver status of the e-mail. Possible values include: "NotSpecified",
     "Enabled", "Disabled".
    :vartype status: str or ~$(python-base-namespace).v2019_03_01.models.ReceiverStatus
    """

    _validation = {
        'name': {'required': True},
        'email_address': {'required': True},
        'use_common_alert_schema': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'use_common_alert_schema': {'key': 'useCommonAlertSchema', 'type': 'bool'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EmailReceiver, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.email_address = kwargs['email_address']
        self.use_common_alert_schema = kwargs['use_common_alert_schema']
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
        **kwargs
    ):
        super(EnableRequest, self).__init__(**kwargs)
        self.receiver_name = kwargs['receiver_name']


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
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


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
        **kwargs
    ):
        super(ItsmReceiver, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.workspace_id = kwargs['workspace_id']
        self.connection_id = kwargs['connection_id']
        self.ticket_configuration = kwargs['ticket_configuration']
        self.region = kwargs['region']


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
    :param use_common_alert_schema: Required. Indicates whether to use common alert schema.
    :type use_common_alert_schema: bool
    """

    _validation = {
        'name': {'required': True},
        'resource_id': {'required': True},
        'callback_url': {'required': True},
        'use_common_alert_schema': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'callback_url': {'key': 'callbackUrl', 'type': 'str'},
        'use_common_alert_schema': {'key': 'useCommonAlertSchema', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LogicAppReceiver, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.resource_id = kwargs['resource_id']
        self.callback_url = kwargs['callback_url']
        self.use_common_alert_schema = kwargs['use_common_alert_schema']


class MetricBaselinesResponse(msrest.serialization.Model):
    """A list of metric baselines.

    :param value: The list of metric baselines.
    :type value: list[~$(python-base-namespace).v2019_03_01.models.SingleMetricBaseline]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SingleMetricBaseline]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MetricBaselinesResponse, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class MetricSingleDimension(msrest.serialization.Model):
    """The metric dimension name and value.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the dimension.
    :type name: str
    :param value: Required. Value of the dimension.
    :type value: str
    """

    _validation = {
        'name': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MetricSingleDimension, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.value = kwargs['value']


class SingleBaseline(msrest.serialization.Model):
    """The baseline values for a single sensitivity value.

    All required parameters must be populated in order to send to Azure.

    :param sensitivity: Required. the sensitivity of the baseline. Possible values include: "Low",
     "Medium", "High".
    :type sensitivity: str or ~$(python-base-namespace).v2019_03_01.models.BaselineSensitivity
    :param low_thresholds: Required. The low thresholds of the baseline.
    :type low_thresholds: list[float]
    :param high_thresholds: Required. The high thresholds of the baseline.
    :type high_thresholds: list[float]
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
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SingleBaseline, self).__init__(**kwargs)
        self.sensitivity = kwargs['sensitivity']
        self.low_thresholds = kwargs['low_thresholds']
        self.high_thresholds = kwargs['high_thresholds']


class SingleMetricBaseline(msrest.serialization.Model):
    """The baseline results of a single metric.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The metric baseline Id.
    :type id: str
    :param type: Required. The resource type of the metric baseline resource.
    :type type: str
    :param name: Required. The name of the metric for which the baselines were retrieved.
    :type name: str
    :param timespan: Required. The timespan for which the data was retrieved. Its value consists of
     two datetimes concatenated, separated by '/'.  This may be adjusted in the future and returned
     back from what was originally requested.
    :type timespan: str
    :param interval: Required. The interval (window size) for which the metric data was returned
     in.  This may be adjusted in the future and returned back from what was originally requested.
     This is not present if a metadata request was made.
    :type interval: ~datetime.timedelta
    :param namespace: The namespace of the metrics been queried.
    :type namespace: str
    :param baselines: Required. The baseline for each time series that was queried.
    :type baselines: list[~$(python-base-namespace).v2019_03_01.models.TimeSeriesBaseline]
    """

    _validation = {
        'id': {'required': True},
        'type': {'required': True},
        'name': {'required': True},
        'timespan': {'required': True},
        'interval': {'required': True},
        'baselines': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'timespan': {'key': 'properties.timespan', 'type': 'str'},
        'interval': {'key': 'properties.interval', 'type': 'duration'},
        'namespace': {'key': 'properties.namespace', 'type': 'str'},
        'baselines': {'key': 'properties.baselines', 'type': '[TimeSeriesBaseline]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SingleMetricBaseline, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.type = kwargs['type']
        self.name = kwargs['name']
        self.timespan = kwargs['timespan']
        self.interval = kwargs['interval']
        self.namespace = kwargs.get('namespace', None)
        self.baselines = kwargs['baselines']


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
    :vartype status: str or ~$(python-base-namespace).v2019_03_01.models.ReceiverStatus
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
        **kwargs
    ):
        super(SmsReceiver, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.country_code = kwargs['country_code']
        self.phone_number = kwargs['phone_number']
        self.status = None


class TimeSeriesBaseline(msrest.serialization.Model):
    """The baseline values for a single time series.

    All required parameters must be populated in order to send to Azure.

    :param aggregation: Required. The aggregation type of the metric.
    :type aggregation: str
    :param dimensions: The dimensions of this time series.
    :type dimensions: list[~$(python-base-namespace).v2019_03_01.models.MetricSingleDimension]
    :param timestamps: Required. The list of timestamps of the baselines.
    :type timestamps: list[~datetime.datetime]
    :param data: Required. The baseline values for each sensitivity.
    :type data: list[~$(python-base-namespace).v2019_03_01.models.SingleBaseline]
    :param metadata_values: The baseline metadata values.
    :type metadata_values: list[~$(python-base-namespace).v2019_03_01.models.BaselineMetadata]
    """

    _validation = {
        'aggregation': {'required': True},
        'timestamps': {'required': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'aggregation': {'key': 'aggregation', 'type': 'str'},
        'dimensions': {'key': 'dimensions', 'type': '[MetricSingleDimension]'},
        'timestamps': {'key': 'timestamps', 'type': '[iso-8601]'},
        'data': {'key': 'data', 'type': '[SingleBaseline]'},
        'metadata_values': {'key': 'metadataValues', 'type': '[BaselineMetadata]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TimeSeriesBaseline, self).__init__(**kwargs)
        self.aggregation = kwargs['aggregation']
        self.dimensions = kwargs.get('dimensions', None)
        self.timestamps = kwargs['timestamps']
        self.data = kwargs['data']
        self.metadata_values = kwargs.get('metadata_values', None)


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
        **kwargs
    ):
        super(VoiceReceiver, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.country_code = kwargs['country_code']
        self.phone_number = kwargs['phone_number']


class WebhookReceiver(msrest.serialization.Model):
    """A webhook receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the webhook receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param service_uri: Required. The URI where webhooks should be sent.
    :type service_uri: str
    :param use_common_alert_schema: Required. Indicates whether to use common alert schema.
    :type use_common_alert_schema: bool
    """

    _validation = {
        'name': {'required': True},
        'service_uri': {'required': True},
        'use_common_alert_schema': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
        'use_common_alert_schema': {'key': 'useCommonAlertSchema', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(WebhookReceiver, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.service_uri = kwargs['service_uri']
        self.use_common_alert_schema = kwargs['use_common_alert_schema']
