#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Tangible()

	result.template = "object/tangible/deed/vehicle_deed/shared_landspeeder_x34_deed.iff"
	result.attribute_template_id = 2
	result.stfName("pet_deed","landspeeder_x34")		
	
	#### BEGIN MODIFICATIONS ####
	result.setStringAttribute("radial_filename", "radials.deed_datapad")
	result.setStringAttribute("deed_pcd", "object/intangible/vehicle/shared_landspeeder_x34_pcd.iff")
	result.setStringAttribute("deed_mobile", "object/mobile/vehicle/shared_landspeeder_x34.iff")
	####  END MODIFICATIONS  ####
	
	return result