# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import CosmosDBManagementClientConfiguration
from .operations import DatabaseAccountsOperations
from .operations import Operations
from .operations import DatabaseOperations
from .operations import CollectionOperations
from .operations import CollectionRegionOperations
from .operations import DatabaseAccountRegionOperations
from .operations import PercentileSourceTargetOperations
from .operations import PercentileTargetOperations
from .operations import PercentileOperations
from .operations import CollectionPartitionRegionOperations
from .operations import CollectionPartitionOperations
from .operations import PartitionKeyRangeIdOperations
from .operations import PartitionKeyRangeIdRegionOperations
from .operations import SqlResourcesOperations
from .operations import MongoDBResourcesOperations
from .operations import TableResourcesOperations
from .operations import CassandraResourcesOperations
from .operations import GremlinResourcesOperations
from .operations import RestorableDatabaseAccountsOperations
from .operations import NotebookWorkspacesOperations
from .operations import RestorableSqlDatabasesOperations
from .operations import RestorableSqlContainersOperations
from .operations import RestorableSqlResourcesOperations
from .operations import RestorableMongodbDatabasesOperations
from .operations import RestorableMongodbCollectionsOperations
from .operations import RestorableMongodbResourcesOperations
from .operations import CassandraClustersOperations
from .operations import CassandraDataCentersOperations
from .operations import PrivateLinkResourcesOperations
from .operations import PrivateEndpointConnectionsOperations
from .. import models


class CosmosDBManagementClient(object):
    """Azure Cosmos DB Database Service Resource Provider REST API.

    :ivar database_accounts: DatabaseAccountsOperations operations
    :vartype database_accounts: azure.mgmt.cosmosdb.aio.operations.DatabaseAccountsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.cosmosdb.aio.operations.Operations
    :ivar database: DatabaseOperations operations
    :vartype database: azure.mgmt.cosmosdb.aio.operations.DatabaseOperations
    :ivar collection: CollectionOperations operations
    :vartype collection: azure.mgmt.cosmosdb.aio.operations.CollectionOperations
    :ivar collection_region: CollectionRegionOperations operations
    :vartype collection_region: azure.mgmt.cosmosdb.aio.operations.CollectionRegionOperations
    :ivar database_account_region: DatabaseAccountRegionOperations operations
    :vartype database_account_region: azure.mgmt.cosmosdb.aio.operations.DatabaseAccountRegionOperations
    :ivar percentile_source_target: PercentileSourceTargetOperations operations
    :vartype percentile_source_target: azure.mgmt.cosmosdb.aio.operations.PercentileSourceTargetOperations
    :ivar percentile_target: PercentileTargetOperations operations
    :vartype percentile_target: azure.mgmt.cosmosdb.aio.operations.PercentileTargetOperations
    :ivar percentile: PercentileOperations operations
    :vartype percentile: azure.mgmt.cosmosdb.aio.operations.PercentileOperations
    :ivar collection_partition_region: CollectionPartitionRegionOperations operations
    :vartype collection_partition_region: azure.mgmt.cosmosdb.aio.operations.CollectionPartitionRegionOperations
    :ivar collection_partition: CollectionPartitionOperations operations
    :vartype collection_partition: azure.mgmt.cosmosdb.aio.operations.CollectionPartitionOperations
    :ivar partition_key_range_id: PartitionKeyRangeIdOperations operations
    :vartype partition_key_range_id: azure.mgmt.cosmosdb.aio.operations.PartitionKeyRangeIdOperations
    :ivar partition_key_range_id_region: PartitionKeyRangeIdRegionOperations operations
    :vartype partition_key_range_id_region: azure.mgmt.cosmosdb.aio.operations.PartitionKeyRangeIdRegionOperations
    :ivar sql_resources: SqlResourcesOperations operations
    :vartype sql_resources: azure.mgmt.cosmosdb.aio.operations.SqlResourcesOperations
    :ivar mongo_db_resources: MongoDBResourcesOperations operations
    :vartype mongo_db_resources: azure.mgmt.cosmosdb.aio.operations.MongoDBResourcesOperations
    :ivar table_resources: TableResourcesOperations operations
    :vartype table_resources: azure.mgmt.cosmosdb.aio.operations.TableResourcesOperations
    :ivar cassandra_resources: CassandraResourcesOperations operations
    :vartype cassandra_resources: azure.mgmt.cosmosdb.aio.operations.CassandraResourcesOperations
    :ivar gremlin_resources: GremlinResourcesOperations operations
    :vartype gremlin_resources: azure.mgmt.cosmosdb.aio.operations.GremlinResourcesOperations
    :ivar restorable_database_accounts: RestorableDatabaseAccountsOperations operations
    :vartype restorable_database_accounts: azure.mgmt.cosmosdb.aio.operations.RestorableDatabaseAccountsOperations
    :ivar notebook_workspaces: NotebookWorkspacesOperations operations
    :vartype notebook_workspaces: azure.mgmt.cosmosdb.aio.operations.NotebookWorkspacesOperations
    :ivar restorable_sql_databases: RestorableSqlDatabasesOperations operations
    :vartype restorable_sql_databases: azure.mgmt.cosmosdb.aio.operations.RestorableSqlDatabasesOperations
    :ivar restorable_sql_containers: RestorableSqlContainersOperations operations
    :vartype restorable_sql_containers: azure.mgmt.cosmosdb.aio.operations.RestorableSqlContainersOperations
    :ivar restorable_sql_resources: RestorableSqlResourcesOperations operations
    :vartype restorable_sql_resources: azure.mgmt.cosmosdb.aio.operations.RestorableSqlResourcesOperations
    :ivar restorable_mongodb_databases: RestorableMongodbDatabasesOperations operations
    :vartype restorable_mongodb_databases: azure.mgmt.cosmosdb.aio.operations.RestorableMongodbDatabasesOperations
    :ivar restorable_mongodb_collections: RestorableMongodbCollectionsOperations operations
    :vartype restorable_mongodb_collections: azure.mgmt.cosmosdb.aio.operations.RestorableMongodbCollectionsOperations
    :ivar restorable_mongodb_resources: RestorableMongodbResourcesOperations operations
    :vartype restorable_mongodb_resources: azure.mgmt.cosmosdb.aio.operations.RestorableMongodbResourcesOperations
    :ivar cassandra_clusters: CassandraClustersOperations operations
    :vartype cassandra_clusters: azure.mgmt.cosmosdb.aio.operations.CassandraClustersOperations
    :ivar cassandra_data_centers: CassandraDataCentersOperations operations
    :vartype cassandra_data_centers: azure.mgmt.cosmosdb.aio.operations.CassandraDataCentersOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.cosmosdb.aio.operations.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.cosmosdb.aio.operations.PrivateEndpointConnectionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = CosmosDBManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.database_accounts = DatabaseAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.database = DatabaseOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.collection = CollectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.collection_region = CollectionRegionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.database_account_region = DatabaseAccountRegionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.percentile_source_target = PercentileSourceTargetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.percentile_target = PercentileTargetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.percentile = PercentileOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.collection_partition_region = CollectionPartitionRegionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.collection_partition = CollectionPartitionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.partition_key_range_id = PartitionKeyRangeIdOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.partition_key_range_id_region = PartitionKeyRangeIdRegionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_resources = SqlResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.mongo_db_resources = MongoDBResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.table_resources = TableResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cassandra_resources = CassandraResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gremlin_resources = GremlinResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_database_accounts = RestorableDatabaseAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notebook_workspaces = NotebookWorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_sql_databases = RestorableSqlDatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_sql_containers = RestorableSqlContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_sql_resources = RestorableSqlResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_mongodb_databases = RestorableMongodbDatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_mongodb_collections = RestorableMongodbCollectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_mongodb_resources = RestorableMongodbResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cassandra_clusters = CassandraClustersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cassandra_data_centers = CassandraDataCentersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "CosmosDBManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
