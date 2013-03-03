#!/usr/bin/python
#filename: GenerateSerial.py

serial_number_start = int(raw_input('Serial Number Start: ')) 
serial_number_end = int(raw_input('Serial Number End: '))
sku = raw_input('SKU: ')
upload_date = raw_input('Upload Date (dd/mm/yyyy): ')
expiry_date = raw_input('Expiry Date (dd/mm/yyyy): ')
filename = raw_input('Output Filename: ')


#Product IDs
XAM4B = '9E2B4D3B-30EE-4FC2-BC55-60D36F055E1D'
XAM4R = '2EA13A3E-514F-4048-9ECE-509B1BE77E94'
XAM4W = '09DE466F-B237-48F9-A99F-152D678943EA'
XAM4S = 'DD4C5D43-C6F1-4F0E-88ED-DCF2CAC44767'
XAM4P = '21481558-8410-4139-B40B-231845DC39F4'
XAM4BL = 'FFEB2280-DF62-4DF2-9D2C-7E1E90C3864D'
XAM4OR = '994AE4CA-F934-49BF-9022-8530DECB0D18'
XAM4GR = '3E74427B-F504-4BF1-BDA5-A470D18690EB'
XAM4PU = 'CFC46786-4840-4AFC-9872-4A254BE60010'
XAM8B = '280922A4-551A-40ED-B04A-ED2DA551C8FA'
XAM8R = 'FA10870B-078E-446F-B7E2-3A922F53FE03'
XAM7B = '5E13A0E5-CED6-45A1-A022-0367A6C89ECE'
XAM7R = '3E03FE2F-F86D-4500-AAB7-CC9E37050A02'
XAM7W = '563AC48B-E835-4A52-98D0-BF9FC64C70B4'
XAM9B = '007E507E-FE42-4534-AE91-ED15669C15FC'
XAM9R = 'D2406AE2-E262-4791-83A8-5893A18A79D6'
XAM5 = '5035E951-48FA-490E-A43C-23D9748DF5C4'
XAM10 = '5FB891B7-3379-4B7B-B159-40A50FC18EE4'

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

#print product_id

# CSV format is serial_number, product_id, upload date, expiry date
f = open(filename, 'w')

for i in range(serial_number_start, serial_number_end):
	if serial_number_start > 999999:
		print >> f, "X%d,%s,%s,%s" % (serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 99999:
		print >> f, "X0%d,%s,%s,%s" % (serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 9999:
		print >> f, "X00%d,%s,%s,%s" % (serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 999:
		print >> f, "X000%d,%s,%s,%s" % (serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 99:
		print >> f, "X0000%d,%s,%s,%s" % (serial_number_start, product_id, upload_date, expiry_date )
	elif serial_number_start > 9:
		print >> f, "X00000%d,%s,%s,%s" % (serial_number_start, product_id, upload_date, expiry_date )
	else:
		print >> f, "X000000%d,%s,%s,%s" % (serial_number_start, product_id, upload_date, expiry_date )

	serial_number_start = serial_number_start + 1
