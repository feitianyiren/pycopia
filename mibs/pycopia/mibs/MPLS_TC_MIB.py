# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, Unsigned32, Integer32
from RFC1213_MIB import transmission
from SNMPv2_TC import TEXTUAL_CONVENTION

class MPLS_TC_MIB(ModuleObject):
	path = '/usr/share/mibs/site/MPLS-TC-MIB'
	conformance = 4
	name = 'MPLS-TC-MIB'
	language = 2
	description = 'This MIB module defines Textual Conventions and\nOBJECT-IDENTITIES for use in documents defining\nmanagement information bases (MIBs) for managing\nMPLS networks.'

# nodes
class mplsMIB(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166])
	name = 'mplsMIB'

class mplsTCMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 1])
	name = 'mplsTCMIB'


# macros
# types 

class MplsAtmVcIdentifier(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(32, 65535))


class MplsBitRate(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(1, 2147483647))
	format = 'd'


class MplsBurstSize(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(1, 4294967295))
	format = 'd'


class MplsExtendedTunnelId(pycopia.SMI.Basetypes.Unsigned32):
	status = 1


class MplsFTNIndex(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(1, 2147483647))


class MplsFTNIndexOrZero(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 2147483647))


class MplsInitialCreationSource(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'snmp'), Enum(3, 'ldp'), Enum(4, 'rsvp'), Enum(5, 'crldp'), Enum(6, 'policyAgent'), Enum(7, 'unknown')]


class MplsLSPID(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 31))


class MplsLabel(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, 4294967295))


class MplsLdpGenAddr(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 64))


class MplsLdpIdentifier(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(6, 6))


class MplsLdpLabelTypes(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'generic'), Enum(2, 'atm'), Enum(3, 'frameRelay')]


class MplsLsrIdentifier(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(4, 4))


class MplsPathIndex(pycopia.SMI.Basetypes.Unsigned32):
	status = 1


class MplsPathIndexOrZero(pycopia.SMI.Basetypes.Unsigned32):
	status = 1


class MplsPortNumber(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 65535))


class MplsTunnelAffinity(pycopia.SMI.Basetypes.Unsigned32):
	status = 1


class MplsTunnelIndex(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(1, 65535))


class MplsTunnelInstanceIndex(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, 65535))

# scalars 
# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
