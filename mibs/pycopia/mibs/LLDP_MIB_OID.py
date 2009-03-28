# python
# This file is generated by a program (mib2py). 

import LLDP_MIB

OIDMAP = {
'1.0.8802.1.1.2': LLDP_MIB.lldpMIB,
'1.0.8802.1.1.2.0': LLDP_MIB.lldpNotifications,
'1.0.8802.1.1.2.0.0': LLDP_MIB.lldpNotificationPrefix,
'1.0.8802.1.1.2.1': LLDP_MIB.lldpObjects,
'1.0.8802.1.1.2.1.1': LLDP_MIB.lldpConfiguration,
'1.0.8802.1.1.2.1.2': LLDP_MIB.lldpStatistics,
'1.0.8802.1.1.2.1.3': LLDP_MIB.lldpLocalSystemData,
'1.0.8802.1.1.2.1.4': LLDP_MIB.lldpRemoteSystemsData,
'1.0.8802.1.1.2.1.5': LLDP_MIB.lldpExtensions,
'1.0.8802.1.1.2.2': LLDP_MIB.lldpConformance,
'1.0.8802.1.1.2.2.1': LLDP_MIB.lldpCompliances,
'1.0.8802.1.1.2.2.2': LLDP_MIB.lldpGroups,
'1.0.8802.1.1.2.1.1.1': LLDP_MIB.lldpMessageTxInterval,
'1.0.8802.1.1.2.1.1.2': LLDP_MIB.lldpMessageTxHoldMultiplier,
'1.0.8802.1.1.2.1.1.3': LLDP_MIB.lldpReinitDelay,
'1.0.8802.1.1.2.1.1.4': LLDP_MIB.lldpTxDelay,
'1.0.8802.1.1.2.1.1.5': LLDP_MIB.lldpNotificationInterval,
'1.0.8802.1.1.2.1.2.1': LLDP_MIB.lldpStatsRemTablesLastChangeTime,
'1.0.8802.1.1.2.1.2.2': LLDP_MIB.lldpStatsRemTablesInserts,
'1.0.8802.1.1.2.1.2.3': LLDP_MIB.lldpStatsRemTablesDeletes,
'1.0.8802.1.1.2.1.2.4': LLDP_MIB.lldpStatsRemTablesDrops,
'1.0.8802.1.1.2.1.2.5': LLDP_MIB.lldpStatsRemTablesAgeouts,
'1.0.8802.1.1.2.1.3.1': LLDP_MIB.lldpLocChassisIdSubtype,
'1.0.8802.1.1.2.1.3.2': LLDP_MIB.lldpLocChassisId,
'1.0.8802.1.1.2.1.3.3': LLDP_MIB.lldpLocSysName,
'1.0.8802.1.1.2.1.3.4': LLDP_MIB.lldpLocSysDesc,
'1.0.8802.1.1.2.1.3.5': LLDP_MIB.lldpLocSysCapSupported,
'1.0.8802.1.1.2.1.3.6': LLDP_MIB.lldpLocSysCapEnabled,
'1.0.8802.1.1.2.1.1.6.1.1': LLDP_MIB.lldpPortConfigPortNum,
'1.0.8802.1.1.2.1.1.6.1.2': LLDP_MIB.lldpPortConfigAdminStatus,
'1.0.8802.1.1.2.1.1.6.1.3': LLDP_MIB.lldpPortConfigNotificationEnable,
'1.0.8802.1.1.2.1.1.6.1.4': LLDP_MIB.lldpPortConfigTLVsTxEnable,
'1.0.8802.1.1.2.1.1.7.1.1': LLDP_MIB.lldpConfigManAddrPortsTxEnable,
'1.0.8802.1.1.2.1.2.6.1.1': LLDP_MIB.lldpStatsTxPortNum,
'1.0.8802.1.1.2.1.2.6.1.2': LLDP_MIB.lldpStatsTxPortFramesTotal,
'1.0.8802.1.1.2.1.2.7.1.1': LLDP_MIB.lldpStatsRxPortNum,
'1.0.8802.1.1.2.1.2.7.1.2': LLDP_MIB.lldpStatsRxPortFramesDiscardedTotal,
'1.0.8802.1.1.2.1.2.7.1.3': LLDP_MIB.lldpStatsRxPortFramesErrors,
'1.0.8802.1.1.2.1.2.7.1.4': LLDP_MIB.lldpStatsRxPortFramesTotal,
'1.0.8802.1.1.2.1.2.7.1.5': LLDP_MIB.lldpStatsRxPortTLVsDiscardedTotal,
'1.0.8802.1.1.2.1.2.7.1.6': LLDP_MIB.lldpStatsRxPortTLVsUnrecognizedTotal,
'1.0.8802.1.1.2.1.2.7.1.7': LLDP_MIB.lldpStatsRxPortAgeoutsTotal,
'1.0.8802.1.1.2.1.3.7.1.1': LLDP_MIB.lldpLocPortNum,
'1.0.8802.1.1.2.1.3.7.1.2': LLDP_MIB.lldpLocPortIdSubtype,
'1.0.8802.1.1.2.1.3.7.1.3': LLDP_MIB.lldpLocPortId,
'1.0.8802.1.1.2.1.3.7.1.4': LLDP_MIB.lldpLocPortDesc,
'1.0.8802.1.1.2.1.3.8.1.1': LLDP_MIB.lldpLocManAddrSubtype,
'1.0.8802.1.1.2.1.3.8.1.2': LLDP_MIB.lldpLocManAddr,
'1.0.8802.1.1.2.1.3.8.1.3': LLDP_MIB.lldpLocManAddrLen,
'1.0.8802.1.1.2.1.3.8.1.4': LLDP_MIB.lldpLocManAddrIfSubtype,
'1.0.8802.1.1.2.1.3.8.1.5': LLDP_MIB.lldpLocManAddrIfId,
'1.0.8802.1.1.2.1.3.8.1.6': LLDP_MIB.lldpLocManAddrOID,
'1.0.8802.1.1.2.1.4.1.1.1': LLDP_MIB.lldpRemTimeMark,
'1.0.8802.1.1.2.1.4.1.1.2': LLDP_MIB.lldpRemLocalPortNum,
'1.0.8802.1.1.2.1.4.1.1.3': LLDP_MIB.lldpRemIndex,
'1.0.8802.1.1.2.1.4.1.1.4': LLDP_MIB.lldpRemChassisIdSubtype,
'1.0.8802.1.1.2.1.4.1.1.5': LLDP_MIB.lldpRemChassisId,
'1.0.8802.1.1.2.1.4.1.1.6': LLDP_MIB.lldpRemPortIdSubtype,
'1.0.8802.1.1.2.1.4.1.1.7': LLDP_MIB.lldpRemPortId,
'1.0.8802.1.1.2.1.4.1.1.8': LLDP_MIB.lldpRemPortDesc,
'1.0.8802.1.1.2.1.4.1.1.9': LLDP_MIB.lldpRemSysName,
'1.0.8802.1.1.2.1.4.1.1.10': LLDP_MIB.lldpRemSysDesc,
'1.0.8802.1.1.2.1.4.1.1.11': LLDP_MIB.lldpRemSysCapSupported,
'1.0.8802.1.1.2.1.4.1.1.12': LLDP_MIB.lldpRemSysCapEnabled,
'1.0.8802.1.1.2.1.4.2.1.1': LLDP_MIB.lldpRemManAddrSubtype,
'1.0.8802.1.1.2.1.4.2.1.2': LLDP_MIB.lldpRemManAddr,
'1.0.8802.1.1.2.1.4.2.1.3': LLDP_MIB.lldpRemManAddrIfSubtype,
'1.0.8802.1.1.2.1.4.2.1.4': LLDP_MIB.lldpRemManAddrIfId,
'1.0.8802.1.1.2.1.4.2.1.5': LLDP_MIB.lldpRemManAddrOID,
'1.0.8802.1.1.2.1.4.3.1.1': LLDP_MIB.lldpRemUnknownTLVType,
'1.0.8802.1.1.2.1.4.3.1.2': LLDP_MIB.lldpRemUnknownTLVInfo,
'1.0.8802.1.1.2.1.4.4.1.1': LLDP_MIB.lldpRemOrgDefInfoOUI,
'1.0.8802.1.1.2.1.4.4.1.2': LLDP_MIB.lldpRemOrgDefInfoSubtype,
'1.0.8802.1.1.2.1.4.4.1.3': LLDP_MIB.lldpRemOrgDefInfoIndex,
'1.0.8802.1.1.2.1.4.4.1.4': LLDP_MIB.lldpRemOrgDefInfo,
'1.0.8802.1.1.2.0.0.1': LLDP_MIB.lldpRemTablesChange,
'1.0.8802.1.1.2.2.2.1': LLDP_MIB.lldpConfigGroup,
'1.0.8802.1.1.2.2.2.2': LLDP_MIB.lldpConfigRxGroup,
'1.0.8802.1.1.2.2.2.3': LLDP_MIB.lldpConfigTxGroup,
'1.0.8802.1.1.2.2.2.4': LLDP_MIB.lldpStatsRxGroup,
'1.0.8802.1.1.2.2.2.5': LLDP_MIB.lldpStatsTxGroup,
'1.0.8802.1.1.2.2.2.6': LLDP_MIB.lldpLocSysGroup,
'1.0.8802.1.1.2.2.2.7': LLDP_MIB.lldpRemSysGroup,
'1.0.8802.1.1.2.2.2.8': LLDP_MIB.lldpNotificationsGroup,
}
