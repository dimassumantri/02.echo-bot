# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import base64
import numpy  as np
import shutil
import SQLdict
import suportingsystem
import seaborn as sns


from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardAction,
    ActivityTypes,
    Attachment,
    AttachmentData,
    Activity,
    ActionTypes,
)
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
from time import sleep
ipheidi = '10.158.234.215'
userheidi = 'npdimas'
passwodjeidi = 'brv7ac'



class EchoBot(ActivityHandler):
    def __init__(self, dirname):
        self.dirname = dirname
        # dirname, filename = os.path.split(os.path.abspath(__file__))
        if os.path.exists(dirname +'/output')==False:
            os.mkdir(dirname +'/output')

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        print(turn_context.activity.from_property)
        # print(turn_context.schema.ConversationAccount)
        if 'PERFORMANCE' in turn_context.activity.text.upper():
            name_user = turn_context.activity.from_property.name
            forbiden_character = ['<','>',':','"','/','|','?','*']
            for chr in forbiden_character:
                if chr in name_user:
                    name_user = name_user.replace(chr, "_")
            if os.path.exists(self.dirname +'/output/' + str(name_user))==False:
                os.mkdir(self.dirname +'/output/' + str(name_user))
            filelist = [ f for f in os.listdir(self.dirname +'/output/' + str(name_user)) if f.endswith(".png") ]
            for f in filelist:
                os.remove(os.path.join(self.dirname +'/output/' + str(name_user), f))
            await self.performance(turn_context,name_user,self.dirname)
            filelist = [ f for f in os.listdir(self.dirname +'/output/' + str(name_user)) if f.endswith(".png") ]
            for f in filelist:
                sendimage = os.path.join(self.dirname +'/output/' + str(name_user), f)
                sleep(0.5)
                await self._handle_outgoing_attachment(turn_context,sendimage)
            # print('tes')
        elif 'RETAKE' in turn_context.activity.text.upper():
            name_user = turn_context.activity.from_property.name
            forbiden_character = ['<','>',':','"','/','|','?','*']
            for chr in forbiden_character:
                if chr in name_user:
                    name_user = name_user.replace(chr, "_")
            filelist = [ f for f in os.listdir(self.dirname +'/output/' + str(name_user)) if f.endswith(".png") ]
            for f in filelist:
                sendimage = os.path.join(self.dirname +'/output/' + str(name_user), f)
                sleep(0.5)
                await self._handle_outgoing_attachment(turn_context,sendimage)
        else:
            # file = r'C:\Users\dsumantr\Documents\02_coding\02_Python Project\LSS_system\Micsf_team\bots/output/5d471751-9675-428d-917b-70f44f9630b0\accessibility.png'
            # await self._handle_outgoing_attachment(turn_context,file)
            # file = r'C:\Users\dsumantr\Documents\02_coding\02_Python Project\LSS_system\Micsf_team\bots\output\5d471751-9675-428d-917b-70f44f9630b0\Cell_Availability.png'
            # await self._handle_outgoing_attachment(turn_context,file)
            # file = r'C:\Users\dsumantr\Documents\02_coding\02_Python Project\LSS_system\Micsf_team\bots\output\5d471751-9675-428d-917b-70f44f9630b0\erab_dueto.png'
            # await self._handle_outgoing_attachment(turn_context,file)
            # file = r'C:\Users\dsumantr\Documents\02_coding\02_Python Project\LSS_system\Micsf_team\bots\output\5d471751-9675-428d-917b-70f44f9630b0\Inter_Freq_HO.png'
            # await self._handle_outgoing_attachment(turn_context,file)
            return await turn_context.send_activity(
                MessageFactory.text(f"Echo: {turn_context.activity.text}")
            )
    async def _handle_outgoing_attachment(self, turn_context: TurnContext,file_path):

        reply = Activity(type=ActivityTypes.message)

        # for file in file_path:
        reply.attachments = [self._get_inline_attachment(file_path)]
        #reply.attachments = [await self._get_upload_attachment(turn_context,file_path)]
        await turn_context.send_activity(reply)

    def _get_inline_attachment(self,file_path) -> Attachment:

        with open(file_path, "rb") as in_file:
            base64_image = base64.b64encode(in_file.read()).decode()

        return Attachment(
            name= file_path.split("/")[-1],
            content_type="image/png",
            content_url=f"data:image/png;base64,{base64_image}",
        )
    async def _get_upload_attachment(self, turn_context: TurnContext,file_path) -> Attachment:
        """
        Creates an "Attachment" to be sent from the bot to the user from an uploaded file.
        :param turn_context:
        :return: Attachment
        """
        with open(file_path, "rb"
        ) as in_file:
            image_data = in_file.read()

        connector = await turn_context.adapter.create_connector_client(
            turn_context.activity.service_url
        )
        conversation_id = turn_context.activity.conversation.id
        response = await connector.conversations.upload_attachment(
            conversation_id,
            AttachmentData(
                name=file_path.split("/")[-1],
                original_base64=image_data,
                type="image/png",
            ),
        )

        base_uri: str = connector.config.base_url
        attachment_uri = (
            base_uri
            + ("" if base_uri.endswith("/") else "/")
            + f"v3/attachments/{response.id}/views/original"
        )

        return Attachment(
            name=file_path.split("/")[-1],
            content_type="image/png",
            content_url=attachment_uri,
        )
    #performance
    async def performance(self,turn_context: TurnContext,id_user,dirname):
        level2G = ['region','mc','site','cell','bsc','agg']
        level3G = ['region','mc','site','cell','rnc','agg']
        level4G = ['region','mc','site','cell','agg']
        region_calue = ['ejro','cjro','ssro','kro','nsro']
        text = turn_context.activity.text.lower()
        if "," in text:
            input = text.split(",")
            if len(input) < 4:
                await turn_context.send_activity( "Hello ,your input is invalid (valid input performance,tech,level,id)  " )
                return
            if input[1].strip() == "2g":
                if input[2].strip() in level2G :
                    report_level = input[2].strip()
                    input_level = input[3].strip()
                    if report_level.lower() == "bsc":
                        inputid = ""
                        for x in input[3:]:
                            inputid = inputid + "," + str(x).strip()
                        inputid = inputid[1:]
                    elif report_level.lower() == "region":
                        if input_level.lower() in region_calue:
                            inputid = input[3].strip()
                        else:
                            mclist = []
                            mcdatalist=[]

                            await turn_context.send_activity( "region is invalid, valid input :" )
                            for y in region_calue:
                                await turn_context.send_activity( "performance,2g,region," + y.upper() )
                            return
                    elif report_level.lower() == "agg":
                        inputsite_agg =""
                        for x in input[3::]:
                            inputsite_agg = inputsite_agg + ",'" + x.strip() + "'"
                        await self.executemcperformance_2G(input[2].strip(),inputsite_agg[1::],turn_context,id_user)
                        return
                    else:
                        inputid = input[3].strip()
                    await self.executemcperformance_2G(input[2].strip(),inputid,turn_context,id_user,dirname)
                else:
                    await turn_context.send_activity( "Hello ,report level you sent is incorrect, availabel level is: region,mc,site,cell,bsc " )
                    return
            elif input[1].strip() == "3g":
                if input[2].strip() in level3G :
                    report_level = input[2].strip()
                    input_level = input[3].strip()
                    if report_level.lower() == "rnc":
                        inputid = ""
                        for x in input[3:]:
                            inputid = inputid + "," + str(x).strip()
                        inputid = inputid[1:]
                    elif report_level.lower() == "region":
                        if input_level.lower() in region_calue:
                            inputid = input[3].strip()
                        else:
                            mclist = []
                            mcdatalist=[]
                            await turn_context.send_activity( "region is invalid, valid input :" )
                            for y in region_calue:
                                await turn_context.send_activity( "performance,3g,region," + y.upper() )
                            return
                    elif report_level.lower() == "agg":
                        inputsite_agg =""
                        for x in input[3::]:
                            inputsite_agg = inputsite_agg + ",'" + x.strip() + "'"
                        await self.executemcperformance_3G(input[2].strip(),inputsite_agg[1::],turn_context,id_user,dirname)
                        return
                    else:
                        inputid = input[3].strip()
                    await self.executemcperformance_3G(input[2].strip(),inputid,turn_context,id_user,dirname)
                else:
                    await turn_context.send_activity( "Hello ,report level you sent is incorrect, availabel level is: region,mc,site,cell,rnc " )
                    return
            elif input[1].strip() == "4g":
                if input[2].strip() in level4G :
                    report_level = input[2].strip()
                    if report_level.lower() == "region":
                        inputid = input[3].strip()
                        if inputid.lower() in region_calue:
                            await self.executemcperformance_4G(input[2].strip(),input[3].strip(),turn_context,id_user)
                        else:
                            mclist=[]
                            mcdatalist=[]
                            await turn_context.send_activity( "region is invalid, valid input :" )
                            for y in region_calue:
                                await turn_context.send_activity( "performance,4g,region," + y.upper() )
                            return
                    elif report_level.lower() == "agg":
                        inputsite_agg =""
                        for x in input[3::]:
                            inputsite_agg = inputsite_agg + ",'" + x.strip() + "'"
                        await self.executemcperformance_4G(input[2].strip(),inputsite_agg[1::],turn_context,id_user,dirname)
                        return
                    else:
                        await self.executemcperformance_4G(input[2].strip(),input[3].strip(),turn_context,id_user,dirname)
                else:
                    await turn_context.send_activity("Hello ,report level you sent is incorrect, availabel level is: region,mc,site,cell,bsc " )
                    return
            else:
                await turn_context.send_activity("Hello ,type of technology you sent is incorrect" )
                return
        else:
            await turn_context.send_activity( "Hello ,Your Input is  not correct. Valid input is (performance,tech,level,id)" )
        return;
    async def executemcperformance_4G(self,querylevel,mcclusterinput,turn_context: TurnContext,name,dirname):

        if querylevel == "mc":
            sqlscript_query = "SELECT MICRO_CLUSTER from isat_report.susy_mc_list"
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            dfclusterlist =  pd.DataFrame(queryresult,columns=fieldnames)
            processingcluster = []
            if "#" in mcclusterinput.upper():#output from Button
                processingcluster.append(mcclusterinput[:-1])
                mcclusterinput = mcclusterinput[:-1]
            else:
                for x in dfclusterlist['MICRO_CLUSTER']:
                    if mcclusterinput.upper() in x.upper() :
                        processingcluster.append(x)
            if len(processingcluster) > 1 :
                # bot.sendMessage(chat_id, "Hello " + name + ",Multiple MC detected, please select one of them" )
                mclist = []
                mcdatalist=[]
                await turn_context.send_activity( "Multiple MC detected, please select one of them" )
                for y in processingcluster:
                    await turn_context.send_activity( "performance,4g,mc," + y )
                return
            elif len(processingcluster) == 0 :
                await turn_context.send_activity( "MC not detected" )
                return
            else:
                mcclusterinput = processingcluster[0]
                sqlscript_query = SQLdict.getSQLScript("4G_MC_perf","")
                sqlscript_query = sqlscript_query +  "and MICRO_CLUSTER = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.MICRO_CLUSTER,a.Band"
                #print(sqlscript_query)
        elif querylevel == "region":
            correctvalue = ['EJRO','CJRO','SSRO','KRO','NSRO']
            for x in correctvalue:
                if mcclusterinput.upper() in x.upper() :
                    mcclusterinput = x
            sqlscript_query = SQLdict.getSQLScript("REGION","")
            sqlscript_query = sqlscript_query +  "and REGION = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.REGION,a.Band"
        elif querylevel == "site":
            yesterday_day = datetime.datetime.today()- datetime.timedelta(hours =24)
            two_days_ago = datetime.datetime.today()- datetime.timedelta(hours =48)
            #check input site id
            sqlscript_query = "SELECT a.SITE_ID  FROM isat_report.susy_4Gperfcell_2 a where (xdate = '" + two_days_ago.strftime("%Y-%m-%d") + "' and xhour = 11 ) or (xdate = '" + yesterday_day.strftime("%Y-%m-%d") + "' and xhour = 18 ) group by a.SITE_ID;"
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            #print(queryresult)
            dfsite = pd.DataFrame(queryresult,columns=fieldnames)
            listofsiteid = dfsite['SITE_ID'].values.tolist()
            siteidinput = mcclusterinput.upper()
            if siteidinput in listofsiteid:
                sqlscript_query = SQLdict.getSQLScript("sitelevel","")
                sqlscript_query = sqlscript_query +  "and SITE_ID = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.SITE_ID,a.Band"
            else:
                await turn_context.send_activity( "id is invalid" )

                return
        elif querylevel == "cell":
            if mcclusterinput.isnumeric() == True :
                sqlscript_query = SQLdict.getSQLScript("mrbtsidlevel","")
                sqlscript_query = sqlscript_query +  "and MRBTS_ID = '" + str(mcclusterinput) + "' GROUP BY a.xDate,a.xHour,a.MICRO_CLUSTER,a.Band,a.MRBTS_ID,a.LNCEL_ID"

                await turn_context.send_activity( "4G cell level statistic also available by passing SITEID as input ID" )
            else:
                yesterday_day = datetime.datetime.today()- datetime.timedelta(hours =24)
                two_days_ago = datetime.datetime.today()- datetime.timedelta(hours =24)
                #check input site id
                sqlscript_query = "SELECT a.SITE_ID  FROM isat_report.susy_4Gperfcell_2 a where (xdate = '" + two_days_ago.strftime("%Y-%m-%d") + "' and xhour = 11 ) or (xdate = '" + yesterday_day.strftime("%Y-%m-%d") + "' and xhour = 18 ) group by a.SITE_ID;"
                queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
                dfsite = pd.DataFrame(queryresult,columns=fieldnames)
                listofsiteid = dfsite['SITE_ID'].values.tolist()
                siteidinput = mcclusterinput.upper()
                if siteidinput in listofsiteid:
                    sqlscript_query = SQLdict.getSQLScript("mrbtsidlevel","")
                    sqlscript_query = sqlscript_query +  "and SITE_ID = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.MICRO_CLUSTER,a.Band,a.MRBTS_ID,a.LNCEL_ID"
                else:
                    await turn_context.send_activity( "id is invalid" )
                    return
        elif querylevel == "agg":
            sqlscript_query = SQLdict.getSQLScript("agg","")
            sqlscript_query = sqlscript_query +  "and SITE_ID in (" + mcclusterinput + ") GROUP BY a.xDate,a.xHour,a.Band"
        try:
            # if os.path.exists(dirname +'/output/' + name + '/Cell_Availability.png'):
            #     os.remove(dirname +'/output/' + name + '/Cell_Availability.png')
            # if os.path.exists(dirname +'/output/' + name + '/accessibility.png'):
            #     os.remove(dirname +'/output/' + name + '/accessibility.png')
            # if os.path.exists(dirname +'/output/' + name + '/retainability.png'):
            #     os.remove(dirname +'/output/' + name + '/retainability.png')
            # if os.path.exists(dirname +'/output/' + name + '/Intra_HO.png'):
            #     os.remove(dirname +'/output/' + name + '/Intra_HO.png')
            # if os.path.exists(dirname +'/output/' + name + '/Inter_Freq_HO.png'):
            #     os.remove(dirname +'/output/' + name + '/Inter_Freq_HO.png')
            # if os.path.exists(dirname +'/output/' + name + '/payload.png'):
            #     os.remove(dirname +'/output/' + name + '/payload.png')
            # if os.path.exists(dirname +'/output/' + name + '/thp.png'):
            #     os.remove(dirname +'/output/' + name + '/thp.png')
            # if os.path.exists(dirname +'/output/' + name + '/erab_dueto.png'):
            #     os.remove(dirname +'/output/' + name + '/erab_dueto.png')
            # if os.path.exists(dirname +'/output/' + name + '/S1_Establisment_SR.png'):
            #     os.remove(dirname +'/output/' + name + '/S1_Establisment_SR.png')
            # if os.path.exists(dirname +'/output/' + name + '/Number_UEs_active_2_Scells.png'):
            #     os.remove(dirname +'/output/' + name + '/Number_UEs_active_2_Scells.png')
            #
            # if os.path.exists(dirname +'/output/' + name + '/RSSI_PUCCH.png'):
            #     os.remove(dirname +'/output/' + name + '/RSSI_PUCCH.png')
            await turn_context.send_activity("Hello ,Your SQL script has been sent to data server" )
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            if len(queryresult) == 0 :
                await turn_context.send_activity('query result is blank, check your input ID')
                return
            df = pd.DataFrame(queryresult,columns=fieldnames)
            df["xDate"] = pd.to_datetime(df["xDate"],format="%Y-%m-%d")
            df["xHour"] = pd.to_timedelta(df['xHour'], unit='H')
            df['Date_hour'] =df['xDate'] + df['xHour']

            if querylevel == "agg" :
                chart_title = "Aggregation"
            else:
                chart_title = mcclusterinput
            mylist=[]
            if querylevel == "cell":
                df['id'] = df['MRBTS_ID'].astype(str) + df['LNCEL_ID'].astype(str)
                mylist = list(dict.fromkeys(df['id']))
            else:
                df['id'] = df['Band'].apply(lambda x: str(x))
                mylist = list(dict.fromkeys(df['Band']))
            sns.set()
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'Cell_Availability', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('Cell_Availability ' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/Cell_Availability.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================

            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                #sns.lineplot( 'Date_hour', 'CSSR', data=dfplot, label = str(x))
                plt.plot( 'Date_hour', 'CSSR', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('CSSR ' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/accessibility.png')

            #sns.figure.savefig(dirname +'/output/' + name + '/accessibility.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:# additional
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'S1_Establisment_SR', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('S1_Establisment_SR ' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/S1_Establisment_SR.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'E-RAB_Drop', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('ERAB Drop ' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/retainability.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'Intra_HO', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('Intra_HO ' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/Intra_HO.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'Inter_Freq_HO', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('Inter_Freq_HO ' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/Inter_Freq_HO.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'Total_Payload(MBytes)', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('Total_Payload(MBytes) ' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/payload.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'LTE_IP_User_Throughput_DL', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('LTE_IP_User_Throughput_DL ' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/thp.png')
            plt.clf()
            plt.cla()
            plt.close()
            #========================================================================= sisni
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'Number_UEs_active_2_Scells', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('Number_UEs_active_2_Scells ' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/Number_UEs_active_2_Scells.png')
            plt.clf()
            plt.cla()
            plt.close()

            #=========================================================================
            if querylevel == "site" or querylevel == "cell":
                for x in mylist:
                    dfplot = df[df['id'].str.contains(str(x))]
                    plt.plot( 'Date_hour', 'RSSI_PUCCH', data=dfplot, label = str(x))
                plt.xticks(rotation=20)
                plt.legend()
                plt.suptitle('RSSI_PUCCH ' + chart_title)
                plt.savefig(dirname +'/output/' + name + '/RSSI_PUCCH.png')
                plt.clf()
                plt.cla()
                plt.close()
            #=========================================================================

            df_plt1 = df.groupby(['Date_hour']).agg({"Radio_Connection_with_UE_lost":'sum', "ERAB_rel_EUTRAN":'sum', "Transp_Res_Unavailable":'sum',"ERAB_rel_fail_Ho_Completion":'sum', "ERAB_insuf_transport_resource":'sum', "ERAB_rel_exp_HO_Guard_Time":'sum', "ERAB_rel_exp_HO_Guard_Time":'sum'}).reset_index()
            plt.plot( 'Date_hour', 'Radio_Connection_with_UE_lost', data=df_plt1, label = "Radio_Connection_with_UE_lost")
            plt.plot( 'Date_hour', 'ERAB_rel_EUTRAN', data=df_plt1, label = "ERAB_rel_EUTRAN")
            plt.plot( 'Date_hour', 'Transp_Res_Unavailable', data=df_plt1, label = "Transp_Res_Unavailable")
            plt.plot( 'Date_hour', 'ERAB_rel_fail_Ho_Completion', data=df_plt1, label = "ERAB_rel_fail_Ho_Completion")
            plt.plot( 'Date_hour', 'ERAB_insuf_transport_resource', data=df_plt1, label = "ERAB_insuf_transport_resource")
            plt.plot( 'Date_hour', 'ERAB_rel_exp_HO_Guard_Time', data=df_plt1, label = "ERAB_rel_exp_HO_Guard_Time")
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('E-RAB Drop Reason' + chart_title)
            plt.savefig(dirname +'/output/' + name + '/erab_dueto.png')
            plt.clf()
            plt.cla()
            plt.close()
            sns.reset_orig()

            # filename = []
            # filename.append(dirname +'/output/' + name + '/Cell_Availability.png')
            # filename.append(dirname +'/output/' + name + '/accessibility.png')
            # filename.append(dirname +'/output/' + name + '/S1_Establisment_SR.png')
            # filename.append(dirname +'/output/' + name + '/retainability.png')
            # # self._handle_outgoing_attachment(turn_context,filename)
            # # filename = []
            # filename.append(dirname +'/output/' + name + '/Intra_HO.png')
            # filename.append(dirname +'/output/' + name + '/Inter_Freq_HO.png')
            # filename.append(dirname +'/output/' + name + '/payload.png')
            # filename.append(dirname +'/output/' + name + '/thp.png')
            # # self._handle_outgoing_attachment(turn_context,filename)
            # # filename = []
            # filename.append(dirname +'/output/' + name + '/payload.png')
            # filename.append(dirname +'/output/' + name + '/Number_UEs_active_2_Scells.png')
            # if querylevel == "site" or querylevel == "cell":
            #     filename.append(dirname +'/output/' + name + '/RSSI_PUCCH.png')
            # filename.append(dirname +'/output/' + name + '/erab_dueto.png')

            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/Cell_Availability.png')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/accessibility.png')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/S1_Establisment_SR.png')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/retainability.png')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/Intra_HO.png')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/Inter_Freq_HO.png')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/payload.png')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/thp.png')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/Number_UEs_active_2_Scells.png')
            # if querylevel == "site" or querylevel == "cell":
            #     self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/RSSI_PUCCH.png')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/erab_dueto.png')
            # await self._handle_outgoing_attachment(turn_context,filename)

            df.to_csv(dirname +'/output/' + name + '/4g_stat_' + name + '.csv', index=None, mode='w')
            # filename.append(dirname +'/output/' + name + '/4g_stat_' + name + '.csv')
            # self._handle_outgoing_attachment(turn_context,dirname +'/output/' + name + '/4g_stat_' + name + '.csv')
            # #bot.sendDocument(chat_id,document=open(dirname +'/output/' + name + '/4g_stat_' + name + '.csv', 'rb'))
            lastmeas = suportingsystem.getlastmeas("4G",ipheidi,userheidi,passwodjeidi)
            print(lastmeas)
            await turn_context.send_activity('completed ' + str(lastmeas) + ', type "retake" to get full result')

        except Exception as err:
            messagerr = 'Failed : '+ str(err)
            print( messagerr)
            return
        print('performance 4g completed ' + str(name))
    async def executemcperformance_3G(self,querylevel,mcclusterinput,turn_context: TurnContext,name,dirname):
        if querylevel == "mc":
            kemaren = datetime.datetime.today()- datetime.timedelta(hours =24)
            duaharikemaren = datetime.datetime.today()- datetime.timedelta(hours =48)
            sqlscript_query = "SELECT MICRO_CLUSTER from isat_report.susy_3gperfcell a where MICRO_CLUSTER is not null and (xdate = '" + kemaren.strftime("%Y-%m-%d") + "' or xdate = '" + duaharikemaren.strftime("%Y-%m-%d") + "') and (xhour = 12 or xhour = 20) group BY a.MICRO_CLUSTER"
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            dfclusterlist =  pd.DataFrame(queryresult,columns=fieldnames)
            processingcluster = []
            if "#" in mcclusterinput.upper():#output from Button
                processingcluster.append(mcclusterinput[:-1])
                mcclusterinput = mcclusterinput[:-1]
            else:
                for x in dfclusterlist['MICRO_CLUSTER']:
                    if mcclusterinput.upper() in x.upper() :
                        processingcluster.append(x)
            if len(processingcluster) > 1 :
                # bot.sendMessage(chat_id, "Hello " + name + ",Multiple MC detected, please select one of them" )
                mclist = []
                mcdatalist=[]
                await turn_context.send_activity( "Multiple MC detected, please select one of them" )
                for y in processingcluster:
                    await turn_context.send_activity( "performance,3g,mc," + y )
                return
                # for y in processingcluster:
                #     bot.sendMessage(chat_id, "performance,3g,mc," + y )
                # return
            elif len(processingcluster) == 0 :
                await turn_context.send_activity( "MC not detected" )
                return
            else:
                mcclusterinput = processingcluster[0]
                sqlscript_query = SQLdict.getSQLScript("3G_MC_perf","")
                sqlscript_query = sqlscript_query +  "and MICRO_CLUSTER = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.MICRO_CLUSTER,a.Band"
        elif querylevel == "region":
            correctvalue = ['EJRO','CJRO','SSRO','KRO','NSRO']
            for x in correctvalue:
                if mcclusterinput.upper() in x.upper() :
                    mcclusterinput = x
            sqlscript_query = SQLdict.getSQLScript("3G_REGION","")
            sqlscript_query = sqlscript_query +  "and REGION = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.REGION,a.Band"
        elif querylevel == "site":
            yesterday_day = datetime.datetime.today()- datetime.timedelta(hours =24)
            two_days_ago = datetime.datetime.today()- datetime.timedelta(hours =24)
            #check input site id
            sqlscript_query = "SELECT a.SITE_ID FROM isat_report.susy_3gperfcell a where (xdate = '" + two_days_ago.strftime("%Y-%m-%d") + "' and xhour = 11 ) or (xdate = '" + yesterday_day.strftime("%Y-%m-%d") + "' and xhour = 18 ) group by a.SITE_ID;"
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            dfsite = pd.DataFrame(queryresult,columns=fieldnames)
            listofsiteid = dfsite['SITE_ID'].values.tolist()
            siteidinput = mcclusterinput.upper()
            if siteidinput in listofsiteid:
                sqlscript_query = SQLdict.getSQLScript("3G_sitelevel","")
                sqlscript_query = sqlscript_query +  "and SITE_ID = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.SITE_ID,a.Band"
            else:
                await turn_context.send_activity( "ID is invalid" )
                return
        elif querylevel == "cell":
            yesterday_day = datetime.datetime.today()- datetime.timedelta(hours =24)
            two_days_ago = datetime.datetime.today()- datetime.timedelta(hours =24)
            #check input site id
            sqlscript_query = "SELECT a.SITE_ID  FROM isat_report.susy_3Gperfcell a where (xdate = '" + two_days_ago.strftime("%Y-%m-%d") + "' and xhour = 11 ) or (xdate = '" + yesterday_day.strftime("%Y-%m-%d") + "' and xhour = 18 ) group by a.SITE_ID;"
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            dfsite = pd.DataFrame(queryresult,columns=fieldnames)
            listofsiteid = dfsite['SITE_ID'].values.tolist()
            siteidinput = mcclusterinput.upper()
            if siteidinput in listofsiteid:
                sqlscript_query = SQLdict.getSQLScript("3G_celllevel","")
                sqlscript_query = sqlscript_query +  "and SITE_ID = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.MICRO_CLUSTER,a.Band,a.WCEL_ID"
            else:
                await turn_context.send_activity( "Id is invalid" )
                return

        elif querylevel == "rnc":
            sqlscript_query = SQLdict.getSQLScript("3G_RNC","")
            sqlscript_query = sqlscript_query +  " and RNC_ID in (" + str(mcclusterinput) + ") GROUP BY a.xdate, a.xHour, a.RNC_ID"
        elif querylevel == "agg":
            sqlscript_query = SQLdict.getSQLScript("3g_agg","")
            sqlscript_query = sqlscript_query +  "and SITE_ID in (" + mcclusterinput + ") GROUP BY a.xDate,a.xHour,a.Band"
        try:
            # if os.path.exists(dirname +'/output/' + name + '/Cell_Availability.png'):
            #     os.remove(dirname +'/output/' + name + '/Cell_Availability.png')
            # if os.path.exists(dirname +'/output/' + name + '/Traffic_CS.png'):
            #     os.remove(dirname +'/output/' + name + '/Traffic_CS.png')
            # if os.path.exists(dirname +'/output/' + name + '/Traffic_PS_Mbit.png'):
            #     os.remove(dirname +'/output/' + name + '/Traffic_PS_Mbit.png')
            # if os.path.exists(dirname +'/output/' + name + '/HSDPA_User_Thput.png'):
            #     os.remove(dirname +'/output/' + name + '/HSDPA_User_Thput.png')
            # if os.path.exists(dirname +'/output/' + name + '/CSSR_CS.png'):
            #     os.remove(dirname +'/output/' + name + '/CSSR_CS.png')
            # if os.path.exists(dirname +'/output/' + name + '/CSSR_PS.png'):
            #     os.remove(dirname +'/output/' + name + '/CSSR_PS.png')
            # if os.path.exists(dirname +'/output/' + name + '/CDR_CS.png'):
            #     os.remove(dirname +'/output/' + name + '/CDR_CS.png')
            # if os.path.exists(dirname +'/output/' + name + '/CDR_PS.png'):
            #     os.remove(dirname +'/output/' + name + '/CDR_PS.png')
            # if os.path.exists(dirname +'/output/' + name + '/SHO.png'):
            #     os.remove(dirname +'/output/' + name + '/SHO.png')
            # if os.path.exists(dirname +'/output/' + name + '/ISHO.png'):
            #     os.remove(dirname +'/output/' + name + '/ISHO.png')
            # if os.path.exists(dirname +'/output/' + name + '/IFHO.png'):
            #     os.remove(dirname +'/output/' + name + '/IFHO.png')
            # if os.path.exists(dirname +'/output/' + name + '/RTWP.png'):
            #     os.remove(dirname +'/output/' + name + '/RTWP.png')
            await turn_context.send_activity("Hello ,Your SQL script has been sent to data server" )
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            if len(queryresult) == 0 :
                await turn_context.send_activity('query result is blank, check your input ID')
                return
            df = pd.DataFrame(queryresult,columns=fieldnames)
            df["xdate"] = pd.to_datetime(df["xdate"],format="%Y-%m-%d")
            df["xHour"] = pd.to_timedelta(df['xHour'], unit='H')
            df['Date_hour'] =df['xdate'] + df['xHour']
            if querylevel == "agg" :
                chart_title = "Aggregation"
            else:
                chart_title = str(mcclusterinput)
            mylist=[]
            if querylevel == "cell":
                df['id'] = df['WCEL_ID'].apply(lambda x: str(x))
                mylist = list(dict.fromkeys(df['id']))
            elif querylevel == "rnc":
                df['id'] = df['RNC_ID'].apply(lambda x: str(x))
                mylist = list(dict.fromkeys(df['id']))
            else:
                df['id'] = df['Band'].apply(lambda x: str(x))
                mylist = list(dict.fromkeys(df['Band']))
            sns.set()
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'Cell_Availability', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('Cell_Availability ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/Cell_Availability.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================

            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'Traffic_CS', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('Traffic_CS ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/Traffic_CS.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'Traffic_PS_Mbit', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('Traffic_PS_Mbit ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/Traffic_PS_Mbit.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'HSDPA_User_Thput', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('HSDPA_User_Thput ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/HSDPA_User_Thput.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'CSSR_CS', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('CSSR_CS ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/CSSR_CS.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================

            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'CSSR_PS', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('CSSR_PS ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/CSSR_PS.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'CDR_CS', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('CDR_CS ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/CDR_CS.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'CDR_PS', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('CDR_PS ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/CDR_PS.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'SHO', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('SHO ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/SHO.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'ISHO', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('ISHO ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/ISHO.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'IFHO', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('IFHO ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/IFHO.png')
            plt.clf()
            plt.cla()
            plt.close()

            #=========================================================================
            if querylevel == "cell" or querylevel == "site":
                for x in mylist:
                    dfplot = df[df['id'].str.contains(str(x))]
                    plt.plot( 'Date_hour', 'RTWP', data=dfplot, label = str(x))
                plt.xticks(rotation=20)
                plt.legend()
                plt.suptitle('RTWP ' + str(chart_title))
                plt.savefig(dirname +'/output/' + name + '/RTWP.png')
                plt.clf()
                plt.cla()
                plt.close()
            sns.reset_orig()
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/Cell_Availability.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/Traffic_CS.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/Traffic_PS_Mbit.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/HSDPA_User_Thput.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/CSSR_CS.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/CSSR_PS.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/CDR_CS.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/CDR_PS.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/SHO.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/ISHO.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/IFHO.png', 'rb'))
            # if querylevel == "cell" or querylevel == "site":
            #     bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/RTWP.png', 'rb'))
            df.to_csv(dirname +'/output/' + name + '/3g_stat_' + name + '.csv', index=None, mode='w')
            # bot.sendDocument(chat_id,document=open(dirname +'/output/' + name + '/3g_stat_' + name + '.csv', 'rb'))
            lastmeas = suportingsystem.getlastmeas("3G",ipheidi,userheidi,passwodjeidi)
            await turn_context.send_activity('completed ' + str(lastmeas) + ', type "retake" to get full result')
        except Exception as err:
            messagerr = 'Failed : '+ str(err)
            # bot.sendMessage(chat_id, messagerr)
        print('performance 3g completed ' + str(name))
    async def executemcperformance_2G(self,querylevel,mcclusterinput,turn_context: TurnContext,name,dirname):

        if querylevel == "mc":
            kemaren = datetime.datetime.today()- datetime.timedelta(hours =24)
            duaharikemaren = datetime.datetime.today()- datetime.timedelta(hours =48)
            sqlscript_query = "SELECT MICRO_CLUSTER from isat_report.susy_2gperfcell a where MICRO_CLUSTER is not null and (xdate = '" + kemaren.strftime("%Y-%m-%d") + "' or xdate = '" + duaharikemaren.strftime("%Y-%m-%d") + "') and (xhour = 12 or xhour = 20) group BY a.MICRO_CLUSTER"
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            dfclusterlist =  pd.DataFrame(queryresult,columns=fieldnames)
            processingcluster = []
            if "#" in mcclusterinput.upper():#output from Button
                processingcluster.append(mcclusterinput[:-1])
                mcclusterinput = mcclusterinput[:-1]
            else:
                for x in dfclusterlist['MICRO_CLUSTER']:
                    if mcclusterinput.upper() in x.upper() :
                        processingcluster.append(x)
            if len(processingcluster) > 1 :
                # bot.sendMessage(chat_id, "Hello " + name + ",Multiple MC detected, please select one of them" )
                mclist = []
                mcdatalist=[]
                await turn_context.send_activity( "Multiple MC detected, please select one of them" )
                for y in processingcluster:
                    await turn_context.send_activity( "performance,2g,mc," + y )

                return
            elif len(processingcluster) == 0 :
                await turn_context.send_activity( "MC not detected" )
                return
            else:
                mcclusterinput = processingcluster[0]
                sqlscript_query = SQLdict.getSQLScript("2G_MC_perf","")
                sqlscript_query = sqlscript_query +  "and MICRO_CLUSTER = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.MICRO_CLUSTER,a.Band"
        elif querylevel == "region":
            correctvalue = ['EJRO','CJRO','SSRO','KRO','NSRO']
            for x in correctvalue:
                if mcclusterinput.upper() in x.upper() :
                    mcclusterinput = x
            sqlscript_query = SQLdict.getSQLScript("2G_REGION","")
            sqlscript_query = sqlscript_query +  "and REGION = '" + mcclusterinput + "' GROUP BY a.xDate,a.xHour,a.REGION,a.BAND"
        elif querylevel == "site":
            yesterday_day = datetime.datetime.today()- datetime.timedelta(hours =24)
            two_days_ago = datetime.datetime.today()- datetime.timedelta(hours =24)
            #check input site id
            sqlscript_query = "SELECT a.SITE_ID FROM isat_report.susy_2gperfcell a where (xdate = '" + two_days_ago.strftime("%Y-%m-%d") + "' and xhour = 11 ) or (xdate = '" + yesterday_day.strftime("%Y-%m-%d") + "' and xhour = 18 ) group by a.SITE_ID;"
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            dfsite = pd.DataFrame(queryresult,columns=fieldnames)
            listofsiteid = dfsite['SITE_ID'].values.tolist()
            siteidinput = mcclusterinput.upper()
            if siteidinput in listofsiteid:
                sqlscript_query = SQLdict.getSQLScript("2G_sitelevel","")
                sqlscript_query = sqlscript_query +  "and SITE_ID = '" + mcclusterinput + "' GROUP BY a.xDate, a.xHour, a.site_id, a.BAND"

            else:
                await turn_context.send_activity( "ID is invalid" )
                return

        elif querylevel == "cell":
            yesterday_day = datetime.datetime.today()- datetime.timedelta(hours =24)
            two_days_ago = datetime.datetime.today()- datetime.timedelta(hours =24)
            #check input site id
            sqlscript_query = "SELECT a.SITE_ID,BSC_ID,BCF_ID FROM isat_report.susy_2gperfcell a where (xdate = '" + two_days_ago.strftime("%Y-%m-%d") + "' and xhour = 11 ) or (xdate = '" + yesterday_day.strftime("%Y-%m-%d") + "' and xhour = 18 ) group by a.SITE_ID;"
            
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            dfsite = pd.DataFrame(queryresult,columns=fieldnames)
            listofsiteid = dfsite['SITE_ID'].values.tolist()
            siteidinput = mcclusterinput.upper()

            if siteidinput in listofsiteid:
                sqlscript_query = SQLdict.getSQLScript("2G_Cellidlevel","")
                sqlscript_query = sqlscript_query +  " and site_id = '" + str(siteidinput) + "' GROUP BY a.xDate,a.xHour,a.MICRO_CLUSTER,a.BAND,a.BSC_ID,a.BCF_ID,a.BTS_ID,a.CELL_ID"

            else:
                await turn_context.send_activity( "ID is invalid" )
                return
        elif querylevel == "bsc":
            sqlscript_query = SQLdict.getSQLScript("2G_BSClevel","")
            sqlscript_query = sqlscript_query +  "and  BSC_ID in (" + str(mcclusterinput) + ") GROUP BY a.xDate,a.xHour,a.BSC_ID"
        elif querylevel == "agg":
            sqlscript_query = SQLdict.getSQLScript("2g_agg","")
            sqlscript_query = sqlscript_query +  "and SITE_ID in (" + mcclusterinput + ")  GROUP BY a.xDate, a.xHour, a.BAND"
        try:
            # if os.path.exists(dirname +'/output/' + name + '/TASR.png'):
            #     os.remove(dirname +'/output/' + name + '/TASR.png')
            # if os.path.exists(dirname +'/output/' + name + '/SDCCH_DROP.png'):
            #     os.remove(dirname +'/output/' + name + '/SDCCH_DROP.png')
            # if os.path.exists(dirname +'/output/' + name + '/DLQUAL0_5.png'):
            #     os.remove(dirname +'/output/' + name + '/DLQUAL0_5.png')
            # if os.path.exists(dirname +'/output/' + name + '/ULQUAL0_5.png'):
            #     os.remove(dirname +'/output/' + name + '/ULQUAL0_5.png')
            # if os.path.exists(dirname +'/output/' + name + '/tch_avail.png'):
            #     os.remove(dirname +'/output/' + name + '/tch_avail.png')
            # if os.path.exists(dirname +'/output/' + name + '/TBF_DROP.png'):
            #     os.remove(dirname +'/output/' + name + '/TBF_DROP.png')
            # if os.path.exists(dirname +'/output/' + name + '/CSSR.png'):
            #     os.remove(dirname +'/output/' + name + '/CSSR.png')
            # if os.path.exists(dirname +'/output/' + name + '/gsm_data_total_traffic_DL.png'):
            #     os.remove(dirname +'/output/' + name + '/gsm_data_total_traffic_DL.png')
            # if os.path.exists(dirname +'/output/' + name + '/Drop_Call_Rate_2.png'):
            #     os.remove(dirname +'/output/' + name + '/Drop_Call_Rate_2.png')
            # if os.path.exists(dirname +'/output/' + name + '/TCH_Traffic_trf_24c.png'):
            #     os.remove(dirname +'/output/' + name + '/TCH_Traffic_trf_24c.png')
            # if os.path.exists(dirname +'/output/' + name + '/HOSR.png'):
            #     os.remove(dirname +'/output/' + name + '/HOSR.png')
            await turn_context.send_activity("Hello ,Your SQL script has been sent to data server" )
            queryresult,fieldnames = suportingsystem.query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
            if len(queryresult) == 0 :
                await turn_context.send_activity('query result is blank, check your input ID')
                return
            df = pd.DataFrame(queryresult,columns=fieldnames)
            df["xDate"] = pd.to_datetime(df["xDate"],format="%Y-%m-%d")
            df["xHour"] = pd.to_timedelta(df['xHour'], unit='H')
            df['Date_hour'] =df['xDate'] + df['xHour']
            if querylevel == "agg" :
                chart_title = "Aggregation"
            else:
                chart_title = str(mcclusterinput)
            mylist=[]
            if querylevel == "cell":
                df['id'] = df['CELL_ID'].apply(lambda x: str(x))
                mylist = list(dict.fromkeys(df['id']))
            elif querylevel == "bsc":
                df['id'] = df['BSC_ID'].apply(lambda x: str(x))
                mylist = list(dict.fromkeys(df['id']))
            else:
                df['id'] = df['BAND'].apply(lambda x: str(x))
                mylist = list(dict.fromkeys(df['BAND']))
            sns.set()
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'tch_avail', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('tch_avail ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/tch_avail.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'TBF_DROP', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('TBF_DROP ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/TBF_DROP.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================

            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'CSSR', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('CSSR ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/CSSR.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================

            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'gsm_data_total_traffic_DL', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('gsm_data_total_traffic_DL ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/gsm_data_total_traffic_DL.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================

            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'Drop_Call_Rate_2', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('Drop_Call_Rate_2 ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/Drop_Call_Rate_2.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================

            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'TCH_Traffic_trf_24c', data=dfplot, label = str(x))
            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('TCH_Traffic_trf_24c ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/TCH_Traffic_trf_24c.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================

            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'HOSR', data=dfplot, label = str(x))

            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('HOSR ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/HOSR.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'TASR', data=dfplot, label = str(x))

            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('TASR ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/TASR.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'SDCCH_DROP', data=dfplot, label = str(x))

            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('SDCCH_DROP ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/SDCCH_DROP.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'DLQUAL0_5', data=dfplot, label = str(x))

            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('DLQUAL0_5 ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/DLQUAL0_5.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            for x in mylist:
                dfplot = df[df['id'].str.contains(str(x))]
                plt.plot( 'Date_hour', 'ULQUAL0_5', data=dfplot, label = str(x))

            plt.xticks(rotation=20)
            plt.legend()
            plt.suptitle('ULQUAL0_5 ' + str(chart_title))
            plt.savefig(dirname +'/output/' + name + '/ULQUAL0_5.png')
            plt.clf()
            plt.cla()
            plt.close()
            #=========================================================================
            sns.reset_orig()
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/tch_avail.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/TBF_DROP.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/CSSR.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/gsm_data_total_traffic_DL.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/Drop_Call_Rate_2.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/TCH_Traffic_trf_24c.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/HOSR.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/TASR.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/SDCCH_DROP.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/DLQUAL0_5.png', 'rb'))
            # bot.sendPhoto(chat_id,photo=open(dirname +'/output/' + name + '/ULQUAL0_5.png', 'rb'))
            df.to_csv(dirname +'/output/' + name + '/2g_stat_' + name + '.csv', index=None, mode='w')
            # bot.sendDocument(chat_id,document=open(dirname +'/output/' + name + '/2g_stat_' + name + '.csv', 'rb'))
            lastmeas = suportingsystem.getlastmeas("2G",ipheidi,userheidi,passwodjeidi)
            await turn_context.send_activity('completed ' + str(lastmeas) + ', type "retake" to get full result')
        except Exception as err:
            messagerr = 'Failed : '+ str(err)
            # bot.sendMessage(chat_id, messagerr)
        print('performance 2g completed ' + str(name))
