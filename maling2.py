#!/usr/bin/env python3
import time
import asyncio
import sys
import random

require('dotenv').config()

from telethon import TelegramClient, events, utils, Button

api_id = process.env.ID
api_hash = process.env.HASH
sesi_file = 'InfectedMaling'

hasil = '/homesx'



bot = 'KampungMaifamX4Bot'    #bot mepam yang digunakan

with TelegramClient(sesi_file, api_id, api_hash) as client:
   client.loop.run_until_complete(client.send_message(bot, '/homesx'))
    
@client.on(events.NewMessage(from_users=bot))
async def handler(event):
        pesan = event.raw_text

        file = open("homesx.txt","a+")
        if  'Rumah Kosong Warga' in pesan: 
            print('kunjungi rumah warga')
            time.sleep(2)
            #await event.respond('masuk')

            hasil = pesan.split('\n')
            
            print(hasil)
            count = 0
            
            for i in range(1,6):
                await event.respond(hasil[i*5])
                print('kirim')
                file.write(hasil[i*5]+'\n')
                print('maling alamat ke-'+str(i))  
                count+=1            
                #number+=1
            
                if count%5==0:
                    time.sleep(2)
                    await event.respond('/makan_KudapanSuci_1')
                    print('hapus buronan')
                time.sleep(2)
            await event.respond('/homesx')
            file.close()
            return

        if 'Kamu terkurung dalam penjara menjijikkan' in pesan:
            print('kena polisi')
            time.sleep(60)
            await event.respond('/release')
            print('nyogok polisi')
            time.sleep(5)
            await event.respond('/homesx')
            return

        if 'Kamu tidak memiliki cukup' in event.raw_text:
           await event.respond("/restore")
           time.sleep(3)
           #await client.disconnect() 
           return


        if "Yummy" or "Energi berhasil" in event.raw_text:
           await event.respond(hasil) 
           #await client.disconnect() 
           return

        
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')

       
