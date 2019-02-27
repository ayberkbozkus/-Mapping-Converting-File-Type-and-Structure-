#type;no;dateCreated;dateSend;version
#ORDER;00001;20180620151834;20180620152001;1
#line_no;itemCode;itemDescription;price;quantityPerPack;orderedQuantity;unitOfMeasure;deliveryDateLatest
#1;C0001;KarÄ±ÅŸÄ±k Meyveli Kek;1,50;48;50;BOX;06Jul2018
main_head = []
head_value = []
content_head = []
content = []

def tuple_converter(knowledge,value_1,value_2=0):
  for value_1 in knowledge:
    tuple_value_1 = tuple(knowledge[value_1])
    for value_2 in knowledge:
      tuple_value_2 = tuple(knowledge[value_1][value_2])

try:
  input_file = open("input/input.txt", "r") #expected file type csv (Comma-separated values)
  line_number = 0
  expected_line = int(input("Enter input file number :  "))
  while line_number < expected_line:
    lines = input_file.readline()
    if line_number < 1:
      main_head_lines = lines.split(";")
      main_head_lines[-1] = main_head_lines[-1].strip('\n')
      main_head.append(main_head_lines)                            #type;no;dateCreated;dateSend;version
    elif line_number < 2:
      head_value_lines = lines.split(";")
      head_value_lines[-1] = head_value_lines[-1].strip('\n')
      head_value.append(head_value_lines)                          #ORDER;00001;20180620151834;20180620152001;1
    elif line_number < 3:
      content_head_lines = lines.split(";")
      content_head_lines[-1] = content_head_lines[-1].strip('\n')
      content_head.append(content_head_lines)                      #line_no;itemCode;itemDescription;price;quantityPerPack;orderedQuantity;unitOfMeasure;deliveryDateLatest
    else:
      content_lines = lines.split(";")
      content_lines[-1] = content_lines[-1].strip('\n')
      content.append(content_lines)                                #1;C0001;KarÄ±ÅŸÄ±k Meyveli Kek;1,50;48;50;BOX;06Jul2018 
    line_number+=1
  input_file.close()



except FileNotFoundError:
  Print("Böyle bir dosya bulunamadı")

#<order>
#	<header>
#		<type>ORDER</type>
#		<no>00001</no>
#		<dateCreated>20180620151834</dateCreated>
#		<dateSend>20180620152001</dateSend>
#		<version>1</version>
#	</header>
#	<lines>
#		<line>
#		<line_no>1</line_no>
#			<itemCode>C0001</itemCode>
#			<itemDescription>Karışık Meyveli Kek</itemDescription>
#			<price>1,50</price>
#			<quantityPerPack>48</quantityPerPack>
#			<orderedQuantity>50</orderedQuantity>
#			<unitOfMeasure>BOX</unitOfMeasure>
#			<deliveryDateLatest>06Jul2018</deliveryDateLatest>
#		</line>