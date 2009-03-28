# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32, Counter32, NOTIFICATION_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMPv2_TC import TEXTUAL_CONVENTION, TimeStamp, TruthValue
from IANA_ADDRESS_FAMILY_NUMBERS_MIB import AddressFamilyNumbers
from SNMP_FRAMEWORK_MIB import SnmpAdminString

class LLDP_MIB(ModuleObject):
	path = '/usr/share/mibs/site/LLDP-MIB'
	conformance = 2
	name = 'LLDP-MIB'
	language = 2
	description = 'Management Information Base module for LLDP configuration,\nstatistics, local system data and remote systems data\ncomponents.\n\nCopyright (C) IEEE (2004).  This version of this MIB module\nis published as subclause 12.1 of IEEE Std 802.1AB-2004;\nsee the standard itself for full legal notices.'

# nodes
class lldpMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2])
	name = 'lldpMIB'

class lldpNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 0])
	name = 'lldpNotifications'

class lldpNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 0, 0])
	name = 'lldpNotificationPrefix'

class lldpObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1])
	name = 'lldpObjects'

class lldpConfiguration(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1])
	name = 'lldpConfiguration'

class lldpStatistics(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2])
	name = 'lldpStatistics'

class lldpLocalSystemData(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3])
	name = 'lldpLocalSystemData'

class lldpRemoteSystemsData(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4])
	name = 'lldpRemoteSystemsData'

class lldpExtensions(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 5])
	name = 'lldpExtensions'

class lldpConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2])
	name = 'lldpConformance'

class lldpCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 1])
	name = 'lldpCompliances'

class lldpGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 2])
	name = 'lldpGroups'


# macros
# types 

class ZeroBasedCounter32(pycopia.SMI.Basetypes.Gauge32):
	status = 1


class TimeFilter(pycopia.SMI.Basetypes.TimeTicks):
	status = 1


class LldpChassisIdSubtype(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'chassisComponent'), Enum(2, 'interfaceAlias'), Enum(3, 'portComponent'), Enum(4, 'macAddress'), Enum(5, 'networkAddress'), Enum(6, 'interfaceName'), Enum(7, 'local')]


class LldpChassisId(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(1, 255))


class LldpPortIdSubtype(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'interfaceAlias'), Enum(2, 'portComponent'), Enum(3, 'macAddress'), Enum(4, 'networkAddress'), Enum(5, 'interfaceName'), Enum(6, 'agentCircuitId'), Enum(7, 'local')]


class LldpPortId(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(1, 255))


class LldpManAddrIfSubtype(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'unknown'), Enum(2, 'ifIndex'), Enum(3, 'systemPortNumber')]


class LldpManAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(1, 31))


class LldpSystemCapabilitiesMap(pycopia.SMI.Basetypes.BITS):
	status = 1
	enumerations = [Enum(0, 'other'), Enum(1, 'repeater'), Enum(2, 'bridge'), Enum(3, 'wlanAccessPoint'), Enum(4, 'router'), Enum(5, 'telephone'), Enum(6, 'docsisCableDevice'), Enum(7, 'stationOnly')]


class LldpPortNumber(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(1, 4096))
	format = 'd'


class LldpPortList(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 512))

# scalars 
class lldpMessageTxInterval(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class lldpMessageTxHoldMultiplier(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class lldpReinitDelay(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class lldpTxDelay(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class lldpNotificationInterval(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class lldpStatsRemTablesLastChangeTime(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class lldpStatsRemTablesInserts(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 2])
	syntaxobject = ZeroBasedCounter32
	access = 4
	units = 'table entries'


class lldpStatsRemTablesDeletes(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 3])
	syntaxobject = ZeroBasedCounter32
	access = 4
	units = 'table entries'


class lldpStatsRemTablesDrops(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 4])
	syntaxobject = ZeroBasedCounter32
	access = 4
	units = 'table entries'


class lldpStatsRemTablesAgeouts(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 5])
	syntaxobject = ZeroBasedCounter32


class lldpLocChassisIdSubtype(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 1])
	syntaxobject = LldpChassisIdSubtype


class lldpLocChassisId(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 2])
	syntaxobject = LldpChassisId


class lldpLocSysName(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 3])
	syntaxobject = SnmpAdminString


class lldpLocSysDesc(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 4])
	syntaxobject = SnmpAdminString


class lldpLocSysCapSupported(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 5])
	syntaxobject = LldpSystemCapabilitiesMap


class lldpLocSysCapEnabled(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 6])
	syntaxobject = LldpSystemCapabilitiesMap


# columns
class lldpPortConfigPortNum(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 1])
	syntaxobject = LldpPortNumber


class lldpPortConfigAdminStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'txOnly'), Enum(2, 'rxOnly'), Enum(3, 'txAndRx'), Enum(4, 'disabled')]


class lldpPortConfigNotificationEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class lldpPortConfigTLVsTxEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class lldpConfigManAddrPortsTxEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 7, 1, 1])
	syntaxobject = LldpPortList


class lldpStatsTxPortNum(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 1])
	syntaxobject = LldpPortNumber


class lldpStatsTxPortFramesTotal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class lldpStatsRxPortNum(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 1])
	syntaxobject = LldpPortNumber


class lldpStatsRxPortFramesDiscardedTotal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class lldpStatsRxPortFramesErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class lldpStatsRxPortFramesTotal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class lldpStatsRxPortTLVsDiscardedTotal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class lldpStatsRxPortTLVsUnrecognizedTotal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class lldpStatsRxPortAgeoutsTotal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 7])
	syntaxobject = ZeroBasedCounter32


class lldpLocPortNum(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 1])
	syntaxobject = LldpPortNumber


class lldpLocPortIdSubtype(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 2])
	syntaxobject = LldpPortIdSubtype


class lldpLocPortId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 3])
	syntaxobject = LldpPortId


class lldpLocPortDesc(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 4])
	syntaxobject = SnmpAdminString


class lldpLocManAddrSubtype(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 1])
	syntaxobject = AddressFamilyNumbers


class lldpLocManAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 2])
	syntaxobject = LldpManAddress


class lldpLocManAddrLen(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class lldpLocManAddrIfSubtype(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 4])
	syntaxobject = LldpManAddrIfSubtype


class lldpLocManAddrIfId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class lldpLocManAddrOID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class lldpRemTimeMark(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 1])
	syntaxobject = TimeFilter


class lldpRemLocalPortNum(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 2])
	syntaxobject = LldpPortNumber


class lldpRemIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class lldpRemChassisIdSubtype(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 4])
	syntaxobject = LldpChassisIdSubtype


class lldpRemChassisId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 5])
	syntaxobject = LldpChassisId


class lldpRemPortIdSubtype(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 6])
	syntaxobject = LldpPortIdSubtype


class lldpRemPortId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 7])
	syntaxobject = LldpPortId


class lldpRemPortDesc(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 8])
	syntaxobject = SnmpAdminString


class lldpRemSysName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 9])
	syntaxobject = SnmpAdminString


class lldpRemSysDesc(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 10])
	syntaxobject = SnmpAdminString


class lldpRemSysCapSupported(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 11])
	syntaxobject = LldpSystemCapabilitiesMap


class lldpRemSysCapEnabled(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 12])
	syntaxobject = LldpSystemCapabilitiesMap


class lldpRemManAddrSubtype(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 1])
	syntaxobject = AddressFamilyNumbers


class lldpRemManAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 2])
	syntaxobject = LldpManAddress


class lldpRemManAddrIfSubtype(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 3])
	syntaxobject = LldpManAddrIfSubtype


class lldpRemManAddrIfId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class lldpRemManAddrOID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class lldpRemUnknownTLVType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class lldpRemUnknownTLVInfo(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class lldpRemOrgDefInfoOUI(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class lldpRemOrgDefInfoSubtype(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class lldpRemOrgDefInfoIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class lldpRemOrgDefInfo(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


# rows 
class lldpPortConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpPortConfigPortNum], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 6, 1])
	access = 2
	columns = {'lldpPortConfigPortNum': lldpPortConfigPortNum, 'lldpPortConfigAdminStatus': lldpPortConfigAdminStatus, 'lldpPortConfigNotificationEnable': lldpPortConfigNotificationEnable, 'lldpPortConfigTLVsTxEnable': lldpPortConfigTLVsTxEnable}


from LLDP_MIB import lldpLocManAddrSubtype
from LLDP_MIB import lldpLocManAddr
class lldpConfigManAddrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpLocManAddrSubtype, lldpLocManAddr], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 1, 7, 1])
	access = 2
	columns = {'lldpConfigManAddrPortsTxEnable': lldpConfigManAddrPortsTxEnable}


class lldpStatsTxPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpStatsTxPortNum], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 6, 1])
	access = 2
	columns = {'lldpStatsTxPortNum': lldpStatsTxPortNum, 'lldpStatsTxPortFramesTotal': lldpStatsTxPortFramesTotal}


class lldpStatsRxPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpStatsRxPortNum], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 2, 7, 1])
	access = 2
	columns = {'lldpStatsRxPortNum': lldpStatsRxPortNum, 'lldpStatsRxPortFramesDiscardedTotal': lldpStatsRxPortFramesDiscardedTotal, 'lldpStatsRxPortFramesErrors': lldpStatsRxPortFramesErrors, 'lldpStatsRxPortFramesTotal': lldpStatsRxPortFramesTotal, 'lldpStatsRxPortTLVsDiscardedTotal': lldpStatsRxPortTLVsDiscardedTotal, 'lldpStatsRxPortTLVsUnrecognizedTotal': lldpStatsRxPortTLVsUnrecognizedTotal, 'lldpStatsRxPortAgeoutsTotal': lldpStatsRxPortAgeoutsTotal}


class lldpLocPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpLocPortNum], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 7, 1])
	access = 2
	columns = {'lldpLocPortNum': lldpLocPortNum, 'lldpLocPortIdSubtype': lldpLocPortIdSubtype, 'lldpLocPortId': lldpLocPortId, 'lldpLocPortDesc': lldpLocPortDesc}


class lldpLocManAddrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpLocManAddrSubtype, lldpLocManAddr], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 3, 8, 1])
	access = 2
	columns = {'lldpLocManAddrSubtype': lldpLocManAddrSubtype, 'lldpLocManAddr': lldpLocManAddr, 'lldpLocManAddrLen': lldpLocManAddrLen, 'lldpLocManAddrIfSubtype': lldpLocManAddrIfSubtype, 'lldpLocManAddrIfId': lldpLocManAddrIfId, 'lldpLocManAddrOID': lldpLocManAddrOID}


class lldpRemEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 1, 1])
	access = 2
	columns = {'lldpRemTimeMark': lldpRemTimeMark, 'lldpRemLocalPortNum': lldpRemLocalPortNum, 'lldpRemIndex': lldpRemIndex, 'lldpRemChassisIdSubtype': lldpRemChassisIdSubtype, 'lldpRemChassisId': lldpRemChassisId, 'lldpRemPortIdSubtype': lldpRemPortIdSubtype, 'lldpRemPortId': lldpRemPortId, 'lldpRemPortDesc': lldpRemPortDesc, 'lldpRemSysName': lldpRemSysName, 'lldpRemSysDesc': lldpRemSysDesc, 'lldpRemSysCapSupported': lldpRemSysCapSupported, 'lldpRemSysCapEnabled': lldpRemSysCapEnabled}


class lldpRemManAddrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex, lldpRemManAddrSubtype, lldpRemManAddr], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 2, 1])
	access = 2
	columns = {'lldpRemManAddrSubtype': lldpRemManAddrSubtype, 'lldpRemManAddr': lldpRemManAddr, 'lldpRemManAddrIfSubtype': lldpRemManAddrIfSubtype, 'lldpRemManAddrIfId': lldpRemManAddrIfId, 'lldpRemManAddrOID': lldpRemManAddrOID}


class lldpRemUnknownTLVEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex, lldpRemUnknownTLVType], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 3, 1])
	access = 2
	columns = {'lldpRemUnknownTLVType': lldpRemUnknownTLVType, 'lldpRemUnknownTLVInfo': lldpRemUnknownTLVInfo}


class lldpRemOrgDefInfoEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex, lldpRemOrgDefInfoOUI, lldpRemOrgDefInfoSubtype, lldpRemOrgDefInfoIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 1, 4, 4, 1])
	access = 2
	columns = {'lldpRemOrgDefInfoOUI': lldpRemOrgDefInfoOUI, 'lldpRemOrgDefInfoSubtype': lldpRemOrgDefInfoSubtype, 'lldpRemOrgDefInfoIndex': lldpRemOrgDefInfoIndex, 'lldpRemOrgDefInfo': lldpRemOrgDefInfo}


# notifications (traps) 
class lldpRemTablesChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 0, 0, 1])

# groups 
class lldpConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 2, 1])
	group = [lldpPortConfigAdminStatus]

class lldpConfigRxGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 2, 2])
	group = [lldpNotificationInterval, lldpPortConfigNotificationEnable]

class lldpConfigTxGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 2, 3])
	group = [lldpMessageTxInterval, lldpMessageTxHoldMultiplier, lldpReinitDelay, lldpTxDelay, lldpPortConfigTLVsTxEnable, lldpConfigManAddrPortsTxEnable]

class lldpStatsRxGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 2, 4])
	group = [lldpStatsRemTablesLastChangeTime, lldpStatsRemTablesInserts, lldpStatsRemTablesDeletes, lldpStatsRemTablesDrops, lldpStatsRemTablesAgeouts, lldpStatsRxPortFramesDiscardedTotal, lldpStatsRxPortFramesErrors, lldpStatsRxPortFramesTotal, lldpStatsRxPortTLVsDiscardedTotal, lldpStatsRxPortTLVsUnrecognizedTotal, lldpStatsRxPortAgeoutsTotal]

class lldpStatsTxGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 2, 5])
	group = [lldpStatsTxPortFramesTotal]

class lldpLocSysGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 2, 6])
	group = [lldpLocChassisIdSubtype, lldpLocChassisId, lldpLocPortIdSubtype, lldpLocPortId, lldpLocPortDesc, lldpLocSysDesc, lldpLocSysName, lldpLocSysCapSupported, lldpLocSysCapEnabled, lldpLocManAddrLen, lldpLocManAddrIfSubtype, lldpLocManAddrIfId, lldpLocManAddrOID]

class lldpRemSysGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 2, 7])
	group = [lldpRemChassisIdSubtype, lldpRemChassisId, lldpRemPortIdSubtype, lldpRemPortId, lldpRemPortDesc, lldpRemSysName, lldpRemSysDesc, lldpRemSysCapSupported, lldpRemSysCapEnabled, lldpRemManAddrIfSubtype, lldpRemManAddrIfId, lldpRemManAddrOID, lldpRemUnknownTLVInfo, lldpRemOrgDefInfo]

class lldpNotificationsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 0, 8802, 1, 1, 2, 2, 2, 8])
	group = [lldpRemTablesChange]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
