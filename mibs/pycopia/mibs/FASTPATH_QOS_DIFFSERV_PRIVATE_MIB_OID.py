# python
# This file is generated by a program (mib2py). 

import FASTPATH_QOS_DIFFSERV_PRIVATE_MIB

OIDMAP = {
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.fastPathQOSDiffServPrivate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusGroup,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassGroup,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyGroup,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServiceGroup,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusAdminMode,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusClassTableSize,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusClassTableMax,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusClassRuleTableSize,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusClassRuleTableMax,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.6': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusPolicyTableSize,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.7': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusPolicyTableMax,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.8': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusPolicyInstTableSize,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.9': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusPolicyInstTableMax,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.10': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusPolicyAttrTableSize,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.11': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusPolicyAttrTableMax,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.12': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusServiceTableSize,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.1.13': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServGenStatusServiceTableMax,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassIndexNextFree,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyIndexNextFree,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.2.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.2.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassName,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.2.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.2.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassAclNum,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.2.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleIndexNextFree,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.2.1.6': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassStorageType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.2.1.7': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.2.1.8': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassAclType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchEntryType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchCos,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchDstIpAddr,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchDstIpMask,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.6': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchDstL4PortStart,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.7': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchDstL4PortEnd,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.8': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchDstMacAddr,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.9': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchDstMacMask,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.10': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchEvery,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.11': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchIpDscp,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.12': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchIpPrecedence,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.13': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchIpTosBits,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.14': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchIpTosMask,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.15': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchProtocolNum,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.16': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchRefClassIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.17': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchSrcIpAddr,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.18': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchSrcIpMask,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.19': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchSrcL4PortStart,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.20': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchSrcL4PortEnd,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.21': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchSrcMacAddr,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.22': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchSrcMacMask,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.23': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchVlanId,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.24': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchExcludeFlag,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.25': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleStorageType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.26': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.27': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchCos2,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.28': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchEtypeKey,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.29': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchEtypeValue,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.30': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchVlanIdStart,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.31': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchVlanIdEnd,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.32': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchVlanId2Start,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.2.3.1.33': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServClassRuleMatchVlanId2End,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.2.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.2.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyName,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.2.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.2.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyInstIndexNextFree,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.2.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyStorageType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.2.1.6': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.3.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyInstIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.3.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyInstClassIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.3.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyInstAttrIndexNextFree,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.3.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyInstStorageType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.3.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyInstRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtEntryType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtBandwidthCrate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtBandwidthCrateUnits,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtExpediteCrate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.6': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtExpediteCrateUnits,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.7': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtExpediteCburst,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.8': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtMarkCosVal,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.9': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtMarkIpDscpVal,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.10': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtMarkIpPrecedenceVal,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.11': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceConformAct,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.12': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceConformVal,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.13': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceExceedAct,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.14': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceExceedVal,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.15': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceNonconformAct,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.16': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceNonconformVal,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.17': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceSimpleCrate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.18': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceSimpleCburst,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.19': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceSinglerateCrate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.20': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceSinglerateCburst,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.21': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceSinglerateEburst,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.22': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceTworateCrate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.23': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceTworateCburst,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.24': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceTworatePrate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.25': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceTworatePburst,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.26': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtRandomdropMinThresh,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.27': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtRandomdropMaxThresh,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.28': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtRandomdropMaxDropProb,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.29': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtRandomdropSamplingRate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.30': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtRandomdropDecayExponent,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.31': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtShapeAverageCrate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.32': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtShapePeakCrate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.33': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtShapePeakPrate,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.34': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStorageType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.35': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.36': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtAssignQueueId,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.37': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtDrop,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.38': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtMarkCos2Val,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.39': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceColorConformIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.40': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceColorConformMode,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.41': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceColorConformVal,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.42': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceColorExceedIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.43': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceColorExceedMode,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.44': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtPoliceColorExceedVal,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.45': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtRedirectIntf,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.4.1.46': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyAttrStmtMirrorIntf,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInOfferedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInOfferedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInDiscardedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInDiscardedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInHCOfferedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.6': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInHCOfferedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.7': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInHCDiscardedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.8': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInHCDiscardedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.9': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInStorageType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.5.1.10': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfInRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutTailDroppedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutTailDroppedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutRandomDroppedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutRandomDroppedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutShapeDelayedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.6': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutShapeDelayedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.7': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutSentOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.8': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutSentPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.9': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutHCTailDroppedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.10': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutHCTailDroppedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.11': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutHCRandomDroppedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.12': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutHCRandomDroppedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.13': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutHCShapeDelayedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.14': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutHCShapeDelayedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.15': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutHCSentOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.16': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutHCSentPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.17': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutStorageType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.3.6.1.18': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServPolicyPerfOutRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.1.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServiceIfIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.1.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServiceIfDirection,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.1.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePolicyIndex,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.1.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServiceIfOperStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.1.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServiceStorageType,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.1.1.6': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServiceRowStatus,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.1': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfOfferedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.2': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfOfferedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.3': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfDiscardedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.4': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfDiscardedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.5': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfSentOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.6': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfSentPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.7': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfHCOfferedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.8': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfHCOfferedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.9': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfHCDiscardedOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.10': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfHCDiscardedPackets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.11': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfHCSentOctets,
'1.3.6.1.4.1.674.10895.5000.2.6132.1.1.7.4.2.1.12': FASTPATH_QOS_DIFFSERV_PRIVATE_MIB.agentDiffServServicePerfHCSentPackets,
}
