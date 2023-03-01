import time

import random

import pandas as pd

import gspread
from gspread_formatting import *
from oauth2client.service_account import ServiceAccountCredentials
import json

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("lucid-course-213904-68ceec697fa3.json", scope)
client = gspread.authorize(creds)
sheet = client.open("(1) Keyword Analysis - ASO TravPart").get_worksheet(4) # Open the spreadhseet
print(' Successfullyy opening file keyword Analysis!')
# Initialize an empty list to store the row indices and an empty dictionary to store the unique names
all_values = sheet.get_all_values()
colA = [row[0] for row in all_values]
colB = [row[1] for row in all_values]
colC = [row[2] for row in all_values]
colE = [row[4] for row in all_values]
colH = [row[7] for row in all_values]
colK = [row[10] for row in all_values]
colDD = [row[3] for row in all_values]


colD = sheet.col_values(4, value_render_option='FORMULA')
colF = sheet.col_values(6, value_render_option='FORMULA')
colG = sheet.col_values(7, value_render_option='FORMULA')
colI = sheet.col_values(9, value_render_option='FORMULA')
colJ = sheet.col_values(10, value_render_option='FORMULA')




time.sleep(random.randrange(1, 3))
print(' Successfullyy get data!')
sheetr = client.open("Content Request").get_worksheet(2)  # Open the spreadhseet
colN = sheetr.col_values(14, value_render_option='FORMULA')
colO = sheetr.col_values(15, value_render_option='FORMULA')
colP = sheetr.col_values(16, value_render_option='FORMULA')
sentenceLD = '''Travpart is for finding a travel partner, hangouts, chat, match and it's a dating apps for adults, but not only you can travel, hookups and hangouts with the travel partner to match but you can also schedule plans and photo which is better than any other dating apps for adults, It's much more convenient than any hangouts or dating apps or hook up apps for adults because it's more flexible to meet up with the partner you need. 

Travpart's Solution : 
A. Hangouts & travel with the people you like similar like a dating apps earnin for adults is no longer difficult 
B. We helps you to find the partner you need swiping up the partner photos like any other social media hookup apps. 
C. You gonna be our video star, adding photo, chatting hangouts for business earnin hookup apps. All of this for free with Travpart earnin dollar general app. 

<b>SOCIAL MEDIA

</b> Social media platform for hangouts chat hookup apps, where you can hangouts with friends moments, post photo, business earnin dating apps for adults. Share best moments by showing your plans at hangouts dollar general app. 
- Enjoy posting and sharing videos to your travel partner
- Hangouts chat & match, similar to a dating apps for adults
- Edits and share photo with followers and travel partner
- Videography and photo through Travpart to show your friends and followers how good you look in the dollar general app. 

<b>HANGOUTS 

</b> It's an app for chatting, earning followers, posting photo, and match with a travel partner. Travpart app is much better than any dating apps for adults chat since it's more convenient. Where you can chat any travel partner you want, no longer need to wait for people to match and earning followers to match you back and with a much simpler algorithm for you to earn followers easy. 

Hangouts &  Dating apps for adults
- Chat 
- Match with a travel partner
- Earn Followers 

<b>ADVERTISE THROUGH A BUSINESS SUITE

</b> You can hangouts with your potential business partner match. 
- Swipe it and match your business partner in dating apps for adults followers providers
- Hangouts and chat with your potential customers match
- No connection issue whatsoever, chat, messages, post photo always send hookup apps. 

<b>BE A VIDEO STAR EARN FOLLOWERS AND MATCH WITH THE PEOPLE YOU LIKE

</b> : Here's what you can do with the videos in Travpart hookup apps followers: 
- See someone you like in a video like any dating apps for adults. 
- Post a video to attract followers to hangouts with you hookup apps 
- Chat with the video star followers dollar general app
- Match with the influencer you like in this dating apps for adults providers 
- Earning Followers easy through the videos dollar general app

<b>TRAVEL MARKET PLACE

</b> Hhookup apps from Road Trip, connect with you by swiping and chatting with you, our dating apps for adults is stacking your phone with trusted travel agency. As you can see in the photos, this hookup apps travel app to enable customers to quickly arrange flight booking, hotel and visit packages. Whether you're looking for adventure/hike locations, best coastal destinations, backpacking, mountain stations, and streams, or the most extraordinary honeymoon destination hookup apps . 
- booking by checking on the relevant photo and video with hookup apps
- Recommends followers places to go, local restaurants food to reserve dining tables by a match of photo hookup apps
- Like any dating apps for adults chat travel with the people match you like Travpart mobile app is allowing you to: 
- Chat with friends through hookup apps 
- Get notifications when friends reaching out in this dating apps for adults and posting photo
- Connect with friends in this hookup apps
- Post photo and browse news, tours, photo hookup apps providers
- Find sites for earnin anywhere to plan a trip with our travel checklist in this dating apps for adults match.
'''
print(' Successfullyy opening file Content Request!')
col1 = "Option"
col2 = "Country"
col3 = "Category"
col4 = "Translated English"
col5 = "Local keyword"
col6 = "AddedE"
col7 = "AddedL"
col8 = "Target"
col9 = "Lack"
col10 = "Density"
col12 = "Send for"
col14 = "LDR"
col15 = "LDF"
col16 = "LDI"
col29 = "LDF"
col30 = "LDI"

time.sleep(random.randrange(10, 20))

#sheetr.update('B1:C1', values_list,values_list1)
sheetr.clear()
cell_list = sheetr.range(f'K1:K{len(colK)}')
for i, val in enumerate(colK):  #gives us a tuple of an index and value
    cell_list[i].value = val    #use the index on cell_list and the val from cell_values

sheetr.update_cells(cell_list)
values = [colA,colB,colC,colD,colE,colF,colG,colH,colI,colJ]
transposed_values = list(map(list, zip(*values)))

valuess = [colN,colO,colP]
transposed_valuess = list(map(list, zip(*valuess)))

sheetr.batch_update([{
    'range': f'A1:J{len(colD)}',
    'values': transposed_values,
}, {
    'range': f'N1:P{len(colD)}',
    'values': transposed_valuess,
}],value_input_option="USER_ENTERED")

print(' Successfullyy insert cols!')

rows = list(zip(colB, colDD))
row_indices = []
unique_names = {}

# Iterate through the rows and cells in the worksheet and search for cells containing the country names
for i, row in enumerate(rows):
    if row[0] not in unique_names:
        # Get the row index of the cell and append it to the list
        row_index = i + 1  # row indices in gspread start at 1
        row_indices.append(row_index)
        # Initialize an empty list for the names for this country in the dictionary
        unique_names[row[0]] = []

# Iterate through the rows and cells in the worksheet again and add the names to the dictionary for each country
for i, row in enumerate(rows):
    if row[0] not in unique_names[row[0]]:
        unique_names[row[0]].append(row[1])


colAC=list(dict.fromkeys(colC))
colAC = colAC[2:]
colADD=len(colAC)
colAD = [i for i in range(1, colADD+1)]
data = pd.DataFrame.from_dict({col29:colAC,col30:colAD},orient='index')
data.transpose()
data_list = data.values.tolist()
sheetr.insert_cols(data_list,29)

time.sleep(random.randrange(5, 10))

dotindex = sentenceLD.find(".")
first_para = sentenceLD[:dotindex]
result1 = [colDD[i-1:j+1] for i, j in zip(row_indices, row_indices[1:])]
result2 = [colK[i-1:j+1] for i, j in zip(row_indices, row_indices[1:])]
countrsymb = ['en','en','en','vi','id','ms','ms','ms','hi','hi','tl','th','ur']
i = 0
j = 0
while i < len(row_indices) and j < len(result1):
    if i == 0 and j == 0:
        i += 1
        j += 1
        continue
    row_index = row_indices[i]
    sublist1 = result1[j]
    sublist2 = result2[j]
    symb = countrsymb[j]
    result = [d for d, l in zip(sublist1, sublist2) if l == "send for Title" or l == "Title" or l == "send for SD"]
    print(*result)
    for value in result:
        if value in first_para:
            print(f"{value} found in first 100 word")
        else:
            print(f"{value} not found in string")
            comma_index = sentenceLD.find(",")
            first_words = sentenceLD[:comma_index]
            rest_of_string = sentenceLD[comma_index:]
            sentenceLD = first_words + ", " + value + rest_of_string

    cell_value = sentenceLD  # Concatenate the sentence and the names list
    row_index1 = str(row_index)
    cell_value2 = '=GOOGLETRANSLATE(AE'+ row_index1 +',"en","'+ symb +'")'  # Concatenate the sentence and the names list
    sheetr.update_cell(row_index, 31, cell_value)  # Update the cell at the specified row index and column
    time.sleep(random.randrange(1, 3))
    sheetr.update_cell(row_index, 41, cell_value2)
    i += 1
    j += 1
print(' Successfullyy insert AE AO cols')

result3 = [colE[i-1:j+1] for i, j in zip(row_indices, row_indices[1:])]
result5 = [colH[i-1:j+1] for i, j in zip(row_indices, row_indices[1:])]
time.sleep(random.randrange(5, 10))
i = 0
j = 0
while i < len(row_indices) and j < len(result3):
    if i == 0 and j == 0:
        i += 1
        j += 1
        continue
    row_index = row_indices[i]
    sublist1 = result3[j]
    sublist2 = result2[j]
    sublist5 = sheetr.cell(row_index, 41).value
    time.sleep(random.randrange(1, 3))
    dotindex = sublist5.find(".")
    first_para = sublist5[:dotindex]
    result = [d for d, l in zip(sublist1,sublist2) if l == "send for Title" or l == "Title" or l == "send for SD"]
    print(*result)
    
    for value in result:
        if value in first_para:
            print(f"{value} found in first 100 word")
        else:
            print(f"{value} not found in string")
            comma_index = sublist5.find(",")
            first_words = sublist5[:comma_index]
            rest_of_string = sublist5[comma_index:]
            sublist5 = first_words + ", " + value + rest_of_string

    cell_value = sublist5  # Concatenate the sentence and the names list
    sheetr.update_cell(row_index, 41, cell_value)
    i += 1
    j += 1

set_row_heights(sheetr, [ ('1:100', 22), ('101:', 22) ])

set_column_widths(sheetr, [ ('A', 200), ('B:', 100) ])
#data = pd.DataFrame.from_dict({col1:noms,col2:prenoms,col3:linkprofiles},orient='index')
#data.transpose()
#data_list = data.values.tolist()
#sheet.insert_cols(data_list)
print(' Successfullyy data save!')


					





