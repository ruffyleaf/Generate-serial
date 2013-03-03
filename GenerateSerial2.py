#!/usr/bin/python
#filename: GenerateSerial2.py
# file is modified with more SKUs and new Serial Number format
# Serial Number anatomy is XF<number><A-Z>

Manufacturer = raw_input('Manufacturer: ')
serial_number_start = int(raw_input('Serial Number Start: ')) 
serial_number_end = int(raw_input('Serial Number End: '))
sku = raw_input('SKU: ')
upload_date = raw_input('Upload Date (dd/mm/yyyy): ')
expiry_date = raw_input('Expiry Date (dd/mm/yyyy): ')
filename = raw_input('Output Filename: ')


#Product IDs
XAM4B		= '9E2B4D3B-30EE-4FC2-BC55-60D36F055E1D'
XAM4R 		= '2EA13A3E-514F-4048-9ECE-509B1BE77E94'
XAM4W 		= '09DE466F-B237-48F9-A99F-152D678943EA'
XAM4S 		= 'DD4C5D43-C6F1-4F0E-88ED-DCF2CAC44767'
XAM4P 		= '21481558-8410-4139-B40B-231845DC39F4'
XAM4BL 		= 'FFEB2280-DF62-4DF2-9D2C-7E1E90C3864D'
XAM4OR 		= '994AE4CA-F934-49BF-9022-8530DECB0D18'
XAM4GR 		= '3E74427B-F504-4BF1-BDA5-A470D18690EB'
XAM4PU 		= 'CFC46786-4840-4AFC-9872-4A254BE60010'
XAM8B 		= '280922A4-551A-40ED-B04A-ED2DA551C8FA'
XAM8R 		= 'FA10870B-078E-446F-B7E2-3A922F53FE03'
XAM7B 		= '5E13A0E5-CED6-45A1-A022-0367A6C89ECE'
XAM7R 		= '3E03FE2F-F86D-4500-AAB7-CC9E37050A02'
XAM7W 		= '563AC48B-E835-4A52-98D0-BF9FC64C70B4'
XAM9B 		= '007E507E-FE42-4534-AE91-ED15669C15FC'
XAM9R 		= 'D2406AE2-E262-4791-83A8-5893A18A79D6'
XAM5 		= '5035E951-48FA-490E-A43C-23D9748DF5C4'
XAM10 		= '5FB891B7-3379-4B7B-B159-40A50FC18EE4'
XAM11		= '481a6a7a-cbf4-4916-b5e8-1f7a50035cce'
XAM14GM 	= '8f141000-2e56-4583-add0-2fb2d2654cc9'
XAM14R 		= '52910a6e-86d0-44df-b2d3-0a23fa0fed37'
XAM14GR 	= 'da191659-6b4e-4b4b-aa98-c113dac421e2'
XAM14PU 	= 'f22f8ab4-189d-4e64-8a64-866e30f74124'
XAM14BL 	= '886cc853-fdd9-42e1-9483-5d6eb896ce96'
XAM14OR 	= '2a921eb3-b485-4bc4-a8aa-14d0bc73638e'
XAM15GM 	= '761e57b3-8147-4a00-8d20-565ab24b65d8'
XAM15R 		= '094a071d-c781-4b97-a779-8472025ae481'
XAM15GR		= '71289cb6-a35d-4231-b9ad-e722eb00df40'
XAM15PU		= 'c0e16ffd-c0dc-44bc-9093-68941a41de2e'
XAM15BL		= '467292c5-3197-46e2-9a48-a548207836ff'
XAM15OR		= '2ba05d45-77b4-4229-97ff-12c0c6188975'

if sku == 'XAM4-B' : product_id = XAM4B
elif sku == 'XAM4-R' : product_id = XAM4R
elif sku == 'XAM4-W' : product_id = XAM4W
elif sku == 'XAM4-S' : product_id = XAM4S
elif sku == 'XAM4-P' : product_id = XAM4P
elif sku == 'XAM4-BL' : product_id = XAM4BL
elif sku == 'XAM4-OR' : product_id = XAM4OR
elif sku == 'XAM4-GR' : product_id = XAM4GR
elif sku == 'XAM4-PU' : proudct_id = XAM4PU
elif sku == 'XAM8-B' : product_id = XAM8B
elif sku == 'XAM8-R' : product_id = XAM8R
elif sku == 'XAM7-B' : product_id = XAM7B
elif sku == 'XAM7-R' : product_id = XAM7R
elif sku == 'XAM7-W' : product_id = XAM7W
elif sku == 'XAM9-B' : product_id = XAM9B
elif sku == 'XAM9-R' : product_id = XAM9R
elif sku == 'XAM5' : product_id = XAM5
elif sku == 'XAM10' : product_id = XAM10
elif sku =='XAM11'	: product_id = XAM11
elif sku =='XAM14-GM' : product_id = XAM14GM
elif sku == 'XAM14-R' : product_id = XAM14R
elif sku == 'XAM14-GR' : product_id = XAM14GR
elif sku == 'XAM14-PU' : product_id = XAM14PU
elif sku == 'XAM14-BL' : product_id = XAM14BL
elif sku == 'XAM14-OR' : product_id = XAM14OR
elif sku == 'XAM15-GM' : product_id = XAM15GM
elif sku == 'XAM15-R' : product_id = XAM15R
elif sku == 'XAM15-GR' : product_id = XAM15GR
elif sku == 'XAM15-PU' : product_id = XAM15PU
elif sku == 'XAM15-BL' : product_id = XAM15BL
elif sku == 'XAM15-OR' : product_id = XAM15OR

#print product_id

# CSV format is serial_number, product_id, upload date, expiry date
f = open(filename, 'w')

for i in range(serial_number_start, serial_number_end):
	if serial_number_start > 999999:
		print >> f, "%s%dA,%s,%s,%s" % (Manufacturer, serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 99999:
		print >> f, "%s0%dA,%s,%s,%s" % (Manufacturer, serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 9999:
		print >> f, "%s00%dA,%s,%s,%s" % (Manufacturer, serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 999:
		print >> f, "%s000%dA,%s,%s,%s" % (Manufacturer, serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 99:
		print >> f, "%s0000%dA,%s,%s,%s" % (Manufacturer, serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 9:
		print >> f, "%s00000%dA,%s,%s,%s" % (Manufacturer, serial_number_start, product_id, upload_date, expiry_date )
	else:
		print >> f, "%s000000%dA,%s,%s,%s" % (Manufacturer, serial_number_start, product_id, upload_date, expiry_date )

	serial_number_start = serial_number_start + 1
