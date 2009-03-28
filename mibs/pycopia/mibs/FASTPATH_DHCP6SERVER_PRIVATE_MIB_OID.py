# python
# This file is generated by a program (mib2py). 

import FASTPATH_DHCP6SERVER_PRIVATE_MIB

OIDMAP = {
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25': FASTPATH_DHCP6SERVER_PRIVATE_MIB.fastPathDHCP6ServerPrivate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerGroup,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolConfigGroup,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceGroup,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingGroup,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerAdminMode,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.2': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerRelayOptParm,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.3': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerRelayOptRemoteIdSuboptParm,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.4': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerDuid,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.5': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerMalformedMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.6': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerDiscardedMessages,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.7': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerSOLICITMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.8': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerREQUESTMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.9': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerCONFIRMMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.10': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerRENEWMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.11': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerREBINDMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.12': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerRELEASEMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.13': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerDECLINEMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.14': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerINFORMREQMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.15': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerRELAYREPLYMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.16': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerRELAYFORWMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.17': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerADVERTISEMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.18': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerREPLYMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.19': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerRECONFIGUREMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.20': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerRELAYREPLYMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.21': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerRELAYFORWMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.1.22': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerClearStatistics,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolNameCreate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.2.1.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.2.1.2': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolName,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.2.1.3': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.2.1.4': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolDnsDomainCreate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.2.1.5': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolDnsServerCreate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.2.1.6': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.4.1.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolDnsDomainIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.4.1.2': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolDnsDomainName,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.4.1.3': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolDnsDomainRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.6.1.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolDnsServerIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.6.1.2': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolDnsServerAddress,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.6.1.3': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolDnsServerRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.7.1.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolAllocationIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.7.1.2': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolAllocationClientIdentifier,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.7.1.3': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolAllocationPrefix,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.7.1.4': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolAllocationPrefixLength,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.7.1.5': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolAllocationClientName,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.7.1.6': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolAllocationIaid,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.7.1.7': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolAllocationValidLifetime,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.7.1.8': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolAllocationPreferLifetime,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.2.7.1.9': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerPoolAllocationRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.1.1.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.1.1.2': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceMode,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.1.1.3': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceServerPoolName,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.1.1.4': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceServerPreference,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.1.1.5': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRelayAddress,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.1.1.6': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRelayInterface,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.1.1.7': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRemoteIdentifier,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.1.1.8': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceOptionFlags,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceStatsIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.2': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceMalformedMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.3': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceDiscardedMessages,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.4': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceSOLICITMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.5': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceREQUESTMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.6': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceCONFIRMMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.7': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRENEWMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.8': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceREBINDMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.9': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRELEASEMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.10': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceDECLINEMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.11': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceINFORMREQMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.12': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRELAYREPLYMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.13': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRELAYFORWMessagesReceived,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.14': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceADVERTISEMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.15': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceREPLYMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.16': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRECONFIGUREMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.17': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRELAYREPLYMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.18': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceRELAYFORWMessagesSent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.3.2.1.19': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6InterfaceClearStatistics,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.1': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.2': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingPrefix,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.3': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingPrefixLength,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.4': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingPrefixType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.5': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingClientIdentifier,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.6': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingClientAddress,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.7': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingClientInterface,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.8': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingIaid,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.9': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingValidLifetime,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.10': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingPreferLifetime,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.25.4.1.1.11': FASTPATH_DHCP6SERVER_PRIVATE_MIB.agentDhcp6ServerBindingExpiration,
}
