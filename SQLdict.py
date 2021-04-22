import datetime
from decimal import *

def getSQLScript(Request,additionalparameter):
    #print(additionalparameter)
    if additionalparameter == "":
        additionalparameter = 0
    hwioffset = int(round(float(additionalparameter),0))
    nowdate = datetime.datetime.today()
    yesterday_day = datetime.datetime.today()- datetime.timedelta(hours =24) # yesterday
    aweekago = datetime.date.today() - datetime.timedelta(hours =168) # seminggu yang lalu
    hwitime = datetime.datetime.today()- datetime.timedelta(hours =int(hwioffset)) # yesterday
    todayminus8hour = datetime.datetime.today()- datetime.timedelta(hours =8)
    twodaysago = datetime.datetime.today()- datetime.timedelta(hours =48)


    if Request == "antennalineconfig" :
        sqlscript_query = """
        SELECT '""" + hwitime.strftime("%Y-%m-%d") + """' as xdate,aa.SIte_ID,aa.mrbts,aa.RMOD_id,aa.serialNumber,aa.productName
        ,if(a.ant_port is NULL ,CONCAT("rx-",d.ant_port),if(d.ant_port is NULL,CONCAT("tx-",a.ant_port),CONCAT("tx-",a.ant_port,"  rx-",d.ant_port))) AS G900_group_A
        ,if(b.ant_port is NULL ,CONCAT('rx-',e.ant_port),if(e.ant_port is NULL,CONCAT('tx-',b.ant_port),CONCAT('tx-',b.ant_port,'  rx-',e.ant_port)))  AS G900_group_B
        ,if(c.ant_port is NULL ,CONCAT('rx-',f.ant_port),if(f.ant_port is NULL,CONCAT('tx-',c.ant_port),CONCAT('tx-',c.ant_port,'  rx-',f.ant_port)))  AS G900_group_C
        ,if(g.ant_port is NULL ,CONCAT('rx-',j.ant_port),if(j.ant_port is NULL,CONCAT('tx-',g.ant_port),CONCAT('tx-',g.ant_port,'  rx-',j.ant_port))) AS U900_group_A
        ,if(h.ant_port is NULL ,CONCAT('rx-',k.ant_port),if(k.ant_port is NULL,CONCAT('tx-',h.ant_port),CONCAT('tx-',h.ant_port,'  rx-',k.ant_port)))  AS U900_group_B
        ,if(i.ant_port is NULL ,CONCAT('rx-',l.ant_port),if(l.ant_port is NULL,CONCAT('tx-',i.ant_port),CONCAT('tx-',i.ant_port,'  rx-',l.ant_port)))  AS U900_group_C
        ,if(m.ant_port is NULL ,CONCAT('rx-',p.ant_port),if(p.ant_port is NULL,CONCAT('tx-',m.ant_port),CONCAT('tx-',m.ant_port,'  rx-',p.ant_port))) AS L900_group_A
        ,if(n.ant_port is NULL ,CONCAT('rx-',q.ant_port),if(q.ant_port is NULL,CONCAT('tx-',n.ant_port),CONCAT('tx-',n.ant_port,'  rx-',q.ant_port)))  AS L900_group_B
        ,if(o.ant_port is NULL ,CONCAT('rx-',r.ant_port),if(r.ant_port is NULL,CONCAT('tx-',o.ant_port),CONCAT('tx-',o.ant_port,'  rx-',r.ant_port)))  AS L900_group_C
        ,if(s.ant_port is NULL ,CONCAT('rx-',v.ant_port),if(v.ant_port is NULL,CONCAT('tx-',s.ant_port),CONCAT('tx-',s.ant_port,'  rx-',v.ant_port))) AS G1800_group_A
        ,if(t.ant_port is NULL ,CONCAT('rx-',w.ant_port),if(w.ant_port is NULL,CONCAT('tx-',t.ant_port),CONCAT('tx-',t.ant_port,'  rx-',w.ant_port)))  AS G1800_group_B
        ,if(u.ant_port is NULL ,CONCAT('rx-',x.ant_port),if(x.ant_port is NULL,CONCAT('tx-',u.ant_port),CONCAT('tx-',u.ant_port,'  rx-',x.ant_port)))  AS G1800_group_C
        ,if(y.ant_port is NULL ,CONCAT('rx-',af.ant_port),if(af.ant_port is NULL,CONCAT('tx-',y.ant_port),CONCAT('tx-',y.ant_port,'  rx-',af.ant_port))) AS L1800_group_A
        ,if(z.ant_port is NULL ,CONCAT('rx-',ag.ant_port),if(ag.ant_port is NULL,CONCAT('tx-',z.ant_port),CONCAT('tx-',z.ant_port,'  rx-',ag.ant_port)))  AS L1800_group_B
        ,if(ae.ant_port is NULL ,CONCAT('rx-',ah.ant_port),if(ah.ant_port is NULL,CONCAT('tx-',ae.ant_port),CONCAT('tx-',ae.ant_port,'  rx-',ah.ant_port)))  AS L1800_group_C
        ,if(ai.ant_port is NULL ,CONCAT('rx-',ao.ant_port),if(ao.ant_port is NULL,CONCAT('tx-',ai.ant_port),CONCAT('tx-',ai.ant_port,'  rx-',ao.ant_port))) AS U2100_group_A
        ,if(aj.ant_port is NULL ,CONCAT('rx-',ap.ant_port),if(ap.ant_port is NULL,CONCAT('tx-',aj.ant_port),CONCAT('tx-',aj.ant_port,'  rx-',ap.ant_port)))  AS U2100_group_B
        ,if(ak.ant_port is NULL ,CONCAT('rx-',aq.ant_port),if(aq.ant_port is NULL,CONCAT('tx-',ak.ant_port),CONCAT('tx-',ak.ant_port,'  rx-',aq.ant_port)))  AS U2100_group_C
        ,if(al.ant_port is NULL ,CONCAT('rx-',ar.ant_port),if(ar.ant_port is NULL,CONCAT('tx-',al.ant_port),CONCAT('tx-',al.ant_port,'  rx-',ar.ant_port)))  AS U2100_group_D
        ,if(am.ant_port is NULL ,CONCAT('rx-',au.ant_port),if(au.ant_port is NULL,CONCAT('tx-',am.ant_port),CONCAT('tx-',am.ant_port,'  rx-',au.ant_port)))  AS U2100_group_E
        ,if(an.ant_port is NULL ,CONCAT('rx-',av.ant_port),if(av.ant_port is NULL,CONCAT('tx-',an.ant_port),CONCAT('tx-',an.ant_port,'  rx-',av.ant_port)))  AS U2100_group_F
        ,if(aw.ant_port is NULL ,CONCAT('rx-',bc.ant_port),if(bc.ant_port is NULL,CONCAT('tx-',aw.ant_port),CONCAT('tx-',aw.ant_port,'  rx-',bc.ant_port))) AS L2100_group_A
        ,if(ax.ant_port is NULL ,CONCAT('rx-',bd.ant_port),if(bd.ant_port is NULL,CONCAT('tx-',ax.ant_port),CONCAT('tx-',ax.ant_port,'  rx-',bd.ant_port)))  AS L2100_group_B
        ,if(ay.ant_port is NULL ,CONCAT('rx-',be.ant_port),if(be.ant_port is NULL,CONCAT('tx-',ay.ant_port),CONCAT('tx-',ay.ant_port,'  rx-',be.ant_port)))  AS L2100_group_C
        ,if(az.ant_port is NULL ,CONCAT('rx-',bf.ant_port),if(bf.ant_port is NULL,CONCAT('tx-',az.ant_port),CONCAT('tx-',az.ant_port,'  rx-',bf.ant_port)))  AS L2100_group_D
        ,if(ba.ant_port is NULL ,CONCAT('rx-',bg.ant_port),if(bg.ant_port is NULL,CONCAT('tx-',ba.ant_port),CONCAT('tx-',ba.ant_port,'  rx-',bg.ant_port)))  AS L2100_group_E
        ,if(bb.ant_port is NULL ,CONCAT('rx-',bh.ant_port),if(bh.ant_port is NULL,CONCAT('tx-',bb.ant_port),CONCAT('tx-',bb.ant_port,'  rx-',bh.ant_port)))  AS L2100_group_F

        FROM isat_report.susy_sitelist_antl aa
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 1 AND a.tech = 'G900' GROUP BY a.grouping) a ON aa.mrbts = a.mrbts AND aa.RMOD_id = a.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 2 AND a.tech = 'G900' GROUP BY a.grouping) b ON aa.mrbts = b.mrbts AND aa.RMOD_id = b.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 3 AND a.tech = 'G900' GROUP BY a.grouping) c ON aa.mrbts = c.mrbts AND aa.RMOD_id = c.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 1 AND a.tech = 'G900' GROUP BY a.grouping) d ON aa.mrbts = d.mrbts AND aa.RMOD_id = d.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 2 AND a.tech = 'G900' GROUP BY a.grouping) e ON aa.mrbts = e.mrbts AND aa.RMOD_id = e.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 3 AND a.tech = 'G900' GROUP BY a.grouping) f ON aa.mrbts = f.mrbts AND aa.RMOD_id = f.RMOD_id



        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 1 AND a.tech = 'U900' GROUP BY a.grouping) g ON aa.mrbts = g.mrbts AND aa.RMOD_id = g.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 2 AND a.tech = 'U900' GROUP BY a.grouping) h ON aa.mrbts = h.mrbts AND aa.RMOD_id = h.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 3 AND a.tech = 'U900' GROUP BY a.grouping) i ON aa.mrbts = i.mrbts AND aa.RMOD_id = i.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 1 AND a.tech = 'U900' GROUP BY a.grouping) j ON aa.mrbts = j.mrbts AND aa.RMOD_id = j.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 2 AND a.tech = 'U900' GROUP BY a.grouping) k ON aa.mrbts = k.mrbts AND aa.RMOD_id = k.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 3 AND a.tech = 'U900' GROUP BY a.grouping) l ON aa.mrbts = l.mrbts AND aa.RMOD_id = l.RMOD_id


        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 1 AND a.tech = 'L900' GROUP BY a.grouping) m ON aa.mrbts = m.mrbts AND aa.RMOD_id = m.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 2 AND a.tech = 'L900' GROUP BY a.grouping) n ON aa.mrbts = n.mrbts AND aa.RMOD_id = n.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 3 AND a.tech = 'L900' GROUP BY a.grouping) o ON aa.mrbts = o.mrbts AND aa.RMOD_id = o.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 1 AND a.tech = 'L900' GROUP BY a.grouping) p ON aa.mrbts = p.mrbts AND aa.RMOD_id = p.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 2 AND a.tech = 'L900' GROUP BY a.grouping) q ON aa.mrbts = q.mrbts AND aa.RMOD_id = q.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 3 AND a.tech = 'L900' GROUP BY a.grouping) r ON aa.mrbts = r.mrbts AND aa.RMOD_id = r.RMOD_id


        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 1 AND a.tech = 'G1800' GROUP BY a.grouping) s ON aa.mrbts = s.mrbts AND aa.RMOD_id = s.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 2 AND a.tech = 'G1800' GROUP BY a.grouping) t ON aa.mrbts = t.mrbts AND aa.RMOD_id = t.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 3 AND a.tech = 'G1800' GROUP BY a.grouping) u ON aa.mrbts = u.mrbts AND aa.RMOD_id = u.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 1 AND a.tech = 'G1800' GROUP BY a.grouping) v ON aa.mrbts = v.mrbts AND aa.RMOD_id = v.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 2 AND a.tech = 'G1800' GROUP BY a.grouping) w ON aa.mrbts = w.mrbts AND aa.RMOD_id = w.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 3 AND a.tech = 'G1800' GROUP BY a.grouping) x ON aa.mrbts = x.mrbts AND aa.RMOD_id = x.RMOD_id

        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 1 AND a.tech = 'L1800' GROUP BY a.grouping) y ON aa.mrbts = y.mrbts AND aa.RMOD_id = y.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 2 AND a.tech = 'L1800' GROUP BY a.grouping) z ON aa.mrbts = z.mrbts AND aa.RMOD_id = z.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 3 AND a.tech = 'L1800' GROUP BY a.grouping) ae ON aa.mrbts = ae.mrbts AND aa.RMOD_id = ae.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 1 AND a.tech = 'L1800' GROUP BY a.grouping) af ON aa.mrbts = af.mrbts AND aa.RMOD_id = af.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 2 AND a.tech = 'L1800' GROUP BY a.grouping) ag ON aa.mrbts = ag.mrbts AND aa.RMOD_id = ag.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 3 AND a.tech = 'L1800' GROUP BY a.grouping) ah ON aa.mrbts = ah.mrbts AND aa.RMOD_id = ah.RMOD_id

        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 1 AND a.tech = 'U2100' GROUP BY a.grouping) ai ON aa.mrbts = ai.mrbts AND aa.RMOD_id = ai.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 2 AND a.tech = 'U2100' GROUP BY a.grouping) aj ON aa.mrbts = aj.mrbts AND aa.RMOD_id = aj.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 3 AND a.tech = 'U2100' GROUP BY a.grouping) ak ON aa.mrbts = ak.mrbts AND aa.RMOD_id = ak.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 4 AND a.tech = 'U2100' GROUP BY a.grouping) al ON aa.mrbts = al.mrbts AND aa.RMOD_id = al.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 5 AND a.tech = 'U2100' GROUP BY a.grouping) am ON aa.mrbts = am.mrbts AND aa.RMOD_id = am.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 6 AND a.tech = 'U2100' GROUP BY a.grouping) an ON aa.mrbts = an.mrbts AND aa.RMOD_id = an.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 1 AND a.tech = 'U2100' GROUP BY a.grouping) ao ON aa.mrbts = ao.mrbts AND aa.RMOD_id = ao.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 2 AND a.tech = 'U2100' GROUP BY a.grouping) ap ON aa.mrbts = ap.mrbts AND aa.RMOD_id = ap.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 3 AND a.tech = 'U2100' GROUP BY a.grouping) aq ON aa.mrbts = aq.mrbts AND aa.RMOD_id = aq.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 4 AND a.tech = 'U2100' GROUP BY a.grouping) ar ON aa.mrbts = ar.mrbts AND aa.RMOD_id = ar.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 5 AND a.tech = 'U2100' GROUP BY a.grouping) au ON aa.mrbts = au.mrbts AND aa.RMOD_id = au.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 6 AND a.tech = 'U2100' GROUP BY a.grouping) av ON aa.mrbts = av.mrbts AND aa.RMOD_id = av.RMOD_id

        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 1 AND a.tech = 'L2100' GROUP BY a.grouping) aw ON aa.mrbts = aw.mrbts AND aa.RMOD_id = aw.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 2 AND a.tech = 'L2100' GROUP BY a.grouping) ax ON aa.mrbts = ax.mrbts AND aa.RMOD_id = ax.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 3 AND a.tech = 'L2100' GROUP BY a.grouping) ay ON aa.mrbts = ay.mrbts AND aa.RMOD_id = ay.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 4 AND a.tech = 'L2100' GROUP BY a.grouping) az ON aa.mrbts = az.mrbts AND aa.RMOD_id = az.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 5 AND a.tech = 'L2100' GROUP BY a.grouping) ba ON aa.mrbts = ba.mrbts AND aa.RMOD_id = ba.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_anttx_config a WHERE a.group_connection = 6 AND a.tech = 'L2100' GROUP BY a.grouping) bb ON aa.mrbts = bb.mrbts AND aa.RMOD_id = bb.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 1 AND a.tech = 'L2100' GROUP BY a.grouping) bc ON aa.mrbts = bc.mrbts AND aa.RMOD_id = bc.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 2 AND a.tech = 'L2100' GROUP BY a.grouping) bd ON aa.mrbts = bd.mrbts AND aa.RMOD_id = bd.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 3 AND a.tech = 'L2100' GROUP BY a.grouping) be ON aa.mrbts = be.mrbts AND aa.RMOD_id = be.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 4 AND a.tech = 'L2100' GROUP BY a.grouping) bf ON aa.mrbts = bf.mrbts AND aa.RMOD_id = bf.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 5 AND a.tech = 'L2100' GROUP BY a.grouping) bg ON aa.mrbts = bg.mrbts AND aa.RMOD_id = bg.RMOD_id
        LEFT JOIN (SELECT a.* from isat_report.susy_antrx_config a WHERE a.group_connection = 6 AND a.tech = 'L2100' GROUP BY a.grouping) bh ON aa.mrbts = bh.mrbts AND aa.RMOD_id = bh.RMOD_id
        GROUP BY aa.mrbts,aa.RMOD_id,aa.serialNumber

        """
    elif Request == "pwi_file_prep" :
        sqlscript_query = """
        Drop table if EXISTS isat_report.susy_sitelist_antltx_alltech_power_sec;
        create TABLE isat_report.susy_sitelist_antltx_alltech_power_sec (
        	`tech` VARCHAR(100) NOT NULL,
        	`SIte_ID` VARCHAR(100) NOT NULL,
        	`grouping2` VARCHAR(100) NOT NULL,
        	`Power_set` MEDIUMINT(9) NULL DEFAULT NULL,
            PRIMARY KEY (tech,SIte_ID,grouping2))
        select a.tech,a.SIte_ID,a.grouping2,group_concat(a.Power SEPARATOR "_") AS Power_set  FROM isat_report.susy_sitelist_antltx_alltech a GROUP BY a.SIte_ID,a.tech,a.grouping2 ORDER BY grouping2 ASC;

        Drop table if EXISTS isat_report.susy_sitelist_antltx_alltech_power_sec2;
        create TABLE isat_report.susy_sitelist_antltx_alltech_power_sec2 (
        	`tech` VARCHAR(100) NOT NULL,
        	`SIte_ID` VARCHAR(100) NOT NULL,
        	`MRBTS` MEDIUMINT(9) NOT NULL,
         `RMOD_id` MEDIUMINT(9) NOT NULL,
        	`Power_set` VARCHAR(20) NULL DEFAULT NULL,
            PRIMARY KEY (tech,SIte_ID,MRBTS,RMOD_id))
        SELECT a.tech,a.SIte_ID,a.mrbts,a.RMOD_id,GROUP_CONCAT(Power_set ORDER BY grouping ASC SEPARATOR  "|") AS Power_set
        FROM(
        select a.tech,a.SIte_ID,a.mrbts,a.RMOD_id,a.grouping,group_concat(a.Power SEPARATOR "_") AS Power_set  FROM isat_report.susy_sitelist_antltx_alltech a where SIte_ID <> "" GROUP BY a.SIte_ID,a.tech,a.grouping ORDER BY grouping ASC)a
        GROUP BY a.SIte_ID,a.tech,mrbts,RMOD_id;
        """
    elif Request == "pwi_file" :
        sqlscript_query = """

        SELECT '""" + hwitime.strftime("%Y-%m-%d") + """' as xdate,XX.*
        ,if (a.Power IS NULL,0,(a.Power)) AS pwr_ANT1
        ,if (b.Power IS NULL,0,(b.Power)) AS pwr_ANT2
        ,if (c.Power IS NULL,0,(c.Power)) AS pwr_ANT3
        ,if (d.Power IS NULL,0,(d.Power)) AS pwr_ANT4
        ,if (e.Power IS NULL,0,(e.Power)) AS pwr_ANT5
        ,if (f.Power IS NULL,0,(f.Power)) AS pwr_ANT6
        ,if (g.Power IS NULL,0,(g.Power)) AS pwr_ANT7
        ,if (h.Power IS NULL,0,(h.Power)) AS pwr_ANT8
        ,if (i.Power IS NULL,0,(i.Power)) AS pwr_ANT9
        ,if (j.Power IS NULL,0,(j.Power)) AS pwr_ANT10
        ,if (k.Power IS NULL,0,(k.Power)) AS pwr_ANT11
        ,if (l.Power IS NULL,0,(l.Power)) AS pwr_ANT12
        ,if (m.Power IS NULL,0,(m.Power)) AS pwr_ANT13
        ,if (n.Power IS NULL,0,(n.Power)) AS pwr_ANT14
        ,if (o.Power IS NULL,0,(o.Power)) AS pwr_ANT15
        ,if (p.Power IS NULL,0,(p.Power)) AS pwr_ANT16
        ,if (q.Power IS NULL,0,(q.Power)) AS pwr_ANT17
        ,if (r.Power IS NULL,0,(r.Power)) AS pwr_ANT18
        ,if( a.Power IS NULL,0,1) +
        if(b.Power IS NULL,0,1) +
        if(c.Power IS NULL,0,1) +
        if(d.Power IS NULL,0,1) +
        if(e.Power IS NULL,0,1) +
        if(f.Power IS NULL,0,1) +
        if(g.Power IS NULL,0,1) +
        if(h.Power IS NULL,0,1) +
        if(i.Power IS NULL,0,1) +
        if(j.Power IS NULL,0,1) +
        if(k.Power IS NULL,0,1) +
        if(l.Power IS NULL,0,1) +
        if(m.Power IS NULL,0,1) +
        if(n.Power IS NULL,0,1) +
        if(o.Power IS NULL,0,1) +
        if(p.Power IS NULL,0,1) +
        if(q.Power IS NULL,0,1) +
        if(r.Power IS NULL,0,1) AS TXcount
        ,a.tech  AS Tech1
        ,b.tech  AS Tech2
        ,c.tech  AS Tech3
        ,d.tech  AS Tech4
        ,e.tech  AS Tech5
        ,f.tech  AS Tech6
        ,g.tech  AS Tech7
        ,h.tech  AS Tech8
        ,i.tech  AS Tech9
        ,j.tech  AS Tech10
        ,k.tech  AS Tech11
        ,l.tech  AS Tech12
        ,m.tech  AS Tech13
        ,n.tech  AS Tech14
        ,o.tech  AS Tech15
        ,p.tech  AS Tech16
        ,q.tech  AS Tech17
        ,r.tech  AS Tech18
        ,GROUP_CONCAT(s.prbutil SEPARATOR "_") as dl_prb_util
        ,GROUP_CONCAT(s.xHour SEPARATOR "|") as xHour_prb
        , powerG9 as Power_G900
        , powerG18 as Power_G1800
        , powerU9 as Power_U900
        , powerU21 as Power_U2100
        , powerL9 as Power_L900
        , powerL18 as Power_L1800
        , powerL21 as Power_L2100


        FROM isat_report.susy_sitelist_antl xx
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 1 GROUP BY a.mrbts,a.RMOD_id) a on xx.mrbts = a.mrbts AND xx.RMOD_id = a.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech  from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 2 GROUP BY a.mrbts,a.RMOD_id) b on xx.mrbts = b.mrbts AND xx.RMOD_id = b.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech  from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 3 GROUP BY a.mrbts,a.RMOD_id) c on xx.mrbts = c.mrbts AND xx.RMOD_id = c.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech  from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 4 GROUP BY a.mrbts,a.RMOD_id) d on xx.mrbts = d.mrbts AND xx.RMOD_id = d.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech  from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 5 GROUP BY a.mrbts,a.RMOD_id) e on xx.mrbts = e.mrbts AND xx.RMOD_id = e.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 6 GROUP BY a.mrbts,a.RMOD_id) f on xx.mrbts = f.mrbts AND xx.RMOD_id = f.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 7 GROUP BY a.mrbts,a.RMOD_id) g on xx.mrbts = g.mrbts AND xx.RMOD_id = g.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 8 GROUP BY a.mrbts,a.RMOD_id) h on xx.mrbts = h.mrbts AND xx.RMOD_id = h.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 9 GROUP BY a.mrbts,a.RMOD_id) i on xx.mrbts = i.mrbts AND xx.RMOD_id = i.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech  from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 10 GROUP BY a.mrbts,a.RMOD_id) j on xx.mrbts = j.mrbts AND xx.RMOD_id = j.RMOD_id

        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 11 GROUP BY a.mrbts,a.RMOD_id) k on xx.mrbts = k.mrbts AND xx.RMOD_id = k.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 12 GROUP BY a.mrbts,a.RMOD_id) l on xx.mrbts = l.mrbts AND xx.RMOD_id = l.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 13 GROUP BY a.mrbts,a.RMOD_id) m on xx.mrbts = m.mrbts AND xx.RMOD_id = m.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech  from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 14 GROUP BY a.mrbts,a.RMOD_id) n on xx.mrbts = n.mrbts AND xx.RMOD_id = n.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech  from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 15 GROUP BY a.mrbts,a.RMOD_id) o on xx.mrbts = o.mrbts AND xx.RMOD_id = o.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech  from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 16 GROUP BY a.mrbts,a.RMOD_id) p on xx.mrbts = p.mrbts AND xx.RMOD_id = p.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 17 GROUP BY a.mrbts,a.RMOD_id) q on xx.mrbts = q.mrbts AND xx.RMOD_id = q.RMOD_id
        left JOIN (SELECT a.mrbts,a.RMOD_id,a.ANTL_id,SUM(a.Power) AS POWER,group_concat(a.tech) AS tech  from isat_report.susy_sitelist_antltx_alltech a WHERE a.ANTL_id = 18 GROUP BY a.mrbts,a.RMOD_id) r on xx.mrbts = r.mrbts AND xx.RMOD_id = r.RMOD_id
        left JOIN  isat_report.susy_prbutil_temporary s On xx.mrbts = s.mrbts AND xx.RMOD_id = s.RMOD_id and xx.SIte_ID = s.SITE_ID

        left JOIN (SELECT tech, SIte_ID,mrbts,rmod_id,Power_set AS powerG9 FROM isat_report.susy_sitelist_antltx_alltech_power_sec2 WHERE tech = 'G900' GROUP BY SIte_ID,tech,mrbts,rmod_id ) aa On xx.SIte_ID = aa.SIte_ID and xx.mrbts = aa.mrbts AND xx.RMOD_id = aa.rmod_id
        left JOIN (SELECT tech, SIte_ID,mrbts,rmod_id,Power_set AS powerG18 FROM isat_report.susy_sitelist_antltx_alltech_power_sec2 WHERE tech = 'G1800' GROUP BY SIte_ID,tech,mrbts,rmod_id ) ab On xx.SIte_ID = ab.SIte_ID and xx.mrbts = ab.mrbts AND xx.RMOD_id = ab.rmod_id
        left JOIN (SELECT tech, SIte_ID,mrbts,rmod_id,Power_set AS powerU9 FROM isat_report.susy_sitelist_antltx_alltech_power_sec2 WHERE tech = 'U900' GROUP BY SIte_ID,tech,mrbts,rmod_id  ) ac On xx.SIte_ID = ac.SIte_ID and xx.mrbts = ac.mrbts AND xx.RMOD_id = ac.rmod_id
        left JOIN (SELECT tech, SIte_ID,mrbts,rmod_id,Power_set AS powerU21 FROM isat_report.susy_sitelist_antltx_alltech_power_sec2 WHERE tech = 'U2100' GROUP BY SIte_ID,tech,mrbts,rmod_id  ) ad On xx.SIte_ID = ad.SIte_ID and xx.mrbts = ad.mrbts AND xx.RMOD_id = ad.rmod_id
        left JOIN (SELECT tech, SIte_ID,mrbts,rmod_id,Power_set AS powerL9 FROM isat_report.susy_sitelist_antltx_alltech_power_sec2 WHERE tech = 'L900' GROUP BY SIte_ID,tech,mrbts,rmod_id  ) ae On xx.SIte_ID = ae.SIte_ID and xx.mrbts = ae.mrbts AND xx.RMOD_id = ae.rmod_id
        left JOIN (SELECT tech, SIte_ID,mrbts,rmod_id,Power_set AS powerL18 FROM isat_report.susy_sitelist_antltx_alltech_power_sec2 WHERE tech = 'L1800' GROUP BY SIte_ID,tech,mrbts,rmod_id  ) af On xx.SIte_ID= af.SIte_ID and xx.mrbts = af.mrbts AND xx.RMOD_id = af.rmod_id
        left JOIN (SELECT tech, SIte_ID,mrbts,rmod_id,Power_set AS powerL21 FROM isat_report.susy_sitelist_antltx_alltech_power_sec2 WHERE tech = 'L2100' GROUP BY SIte_ID,tech,mrbts,rmod_id  ) ag On xx.SIte_ID = ag.SIte_ID and xx.mrbts = ag.mrbts AND xx.RMOD_id = ag.rmod_id

          GROUP BY xx.mrbts,xx.RMOD_id,xx.serialNumber
          """
    elif Request == "pwi_module_prep":
        sqlscript_query = """
        Drop table if EXISTS isat_report.tempbbmod;
        create TABLE isat_report.tempbbmod (
                	`xdate` DATE NOT NULL,
                	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
                	`productName` VARCHAR(50) NULL DEFAULT NULL,
                	`serialNumber` VARCHAR(50)  NULL DEFAULT NULL,
                	PRIMARY KEY (MRBTS,serialNumber))
        			SELECT a.xdate,a.MRBTS,a.productName,a.serialNumber  FROM isat_cm.bbmod_r a
        			WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """' AND serialNumber IS NOT NULL
        			GROUP BY MRBTS,serialNumber;
        Drop table if EXISTS isat_report.tempbbmod2;
        create TABLE isat_report.tempbbmod2 (
                	`Site_id` VARCHAR(50)  NULL DEFAULT NULL,
                	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
                	`serialNumber` VARCHAR(50)  NULL DEFAULT NULL,
                	`productName` VARCHAR(50) NULL DEFAULT NULL,
                	PRIMARY KEY (MRBTS,serialNumber))
        SELECT a.Site_id,a.mrbts,b.serialNumber,if(b.productName = "Flexi Baseband Sub-Module FBBC","FBBC",if(b.productName="BB Extension Outdoor Sub-Module FBBA","FBBA",if(b.productName="ABIA AirScale Capacity","ABIA",b.productName))) AS productName
        FROM isat_report.susy_sitelist_antl a
        JOIN isat_report.tempbbmod b ON b.MRBTS = a.mrbts
        GROUP by a.mrbts,b.serialNumber;
        Drop table if EXISTS isat_report.tempbbmod;


        Drop table if EXISTS isat_report.tempsmod;
        create TABLE isat_report.tempsmod (
                	`xdate` DATE NOT NULL,
                	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
                	`productName` VARCHAR(50) NULL DEFAULT NULL,
                	`serialNumber` VARCHAR(50)  NULL DEFAULT NULL,
                	PRIMARY KEY (MRBTS,serialNumber))
        			SELECT a.xdate,a.MRBTS,a.productName,a.serialNumber  FROM isat_cm.smod_r a
        			WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """' AND serialNumber IS NOT NULL
        			GROUP BY MRBTS,serialNumber;
        Drop table if EXISTS isat_report.tempsmod2;
        create TABLE isat_report.tempsmod2 (
                	`Site_id` VARCHAR(50)  NULL DEFAULT NULL,
                	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
                	`serialNumber` VARCHAR(50)  NULL DEFAULT NULL,
                	`productName` VARCHAR(50) NULL DEFAULT NULL,
                	PRIMARY KEY (MRBTS,serialNumber))
        SELECT a.Site_id,a.mrbts,b.serialNumber,if(b.productName = "Flexi System Module Outdoor FSMF","FSMF",if(b.productName="ASIA AirScale Common","ASIA",b.productName)) AS productName
        FROM isat_report.susy_sitelist_antl a
        JOIN isat_report.tempsmod b ON b.MRBTS = a.mrbts
        GROUP by a.mrbts,b.serialNumber;
        Drop table if EXISTS isat_report.tempsmod;



        Drop table if EXISTS isat_report.temptrmod;
        create TABLE isat_report.temptrmod (
                	`xdate` DATE NOT NULL,
                	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
                	`productName` VARCHAR(50) NULL DEFAULT NULL,
                	`serialNumber` VARCHAR(50)  NULL DEFAULT NULL,
                	PRIMARY KEY (MRBTS,serialNumber))
        			SELECT a.xdate,a.MRBTS,a.productName,a.serialNumber  FROM isat_cm.trmod_r a
        			WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """' AND serialNumber IS NOT null
        			GROUP BY MRBTS,serialNumber;
        Drop table if EXISTS isat_report.temptrmod2;
        create TABLE isat_report.temptrmod2 (
                	`Site_id` VARCHAR(50)  NULL DEFAULT NULL,
                	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
                	`serialNumber` VARCHAR(50)  NULL DEFAULT NULL,
                	`productName` VARCHAR(50) NULL DEFAULT NULL,
                	PRIMARY KEY (MRBTS,serialNumber))
        SELECT a.Site_id,a.mrbts,b.serialNumber, b.productName
        FROM isat_report.susy_sitelist_antl a
        JOIN isat_report.temptrmod b ON b.MRBTS = a.mrbts
        GROUP by a.mrbts,b.serialNumber;
        Drop table if EXISTS isat_report.temptrmod;"""
    elif Request == "pwi_file_module" :
        sqlscript_query = """
        SELECT a.site_id, a.productName AS smod, b.productName AS bbmod, c.productName AS trmod
        , powerG9 as Power_G900
        , powerG18 as Power_G1800
        , powerU9 as Power_U900
        , powerU21 as Power_U2100
        , powerL9 as Power_L900
        , powerL18 as Power_L1800
        , powerL21 as Power_L2100
        FROM (select site_id,group_concat(productName) AS productName from isat_report.tempsmod2 group by site_id) a
        Left JOIN  (select site_id,group_concat(productName) AS productName from isat_report.tempbbmod2 group by site_id) b ON a.site_id = b.site_id
        Left JOIN (select site_id,group_concat(productName) AS productName from isat_report.temptrmod2 group by site_id)  c ON a.site_id = c.site_id
        left JOIN (SELECT tech, SIte_ID,GROUP_CONCAT(Power_set ORDER BY grouping2 ASC SEPARATOR  "|")  AS powerG9 FROM isat_report.susy_sitelist_antltx_alltech_power_sec WHERE tech = 'G900' GROUP BY SIte_ID,tech ) aa On a.site_id = aa.SIte_ID
        left JOIN (SELECT tech, SIte_ID,GROUP_CONCAT(Power_set ORDER BY grouping2 ASC SEPARATOR  "|")  AS powerG18 FROM isat_report.susy_sitelist_antltx_alltech_power_sec WHERE tech = 'G1800' GROUP BY SIte_ID,tech ) ab On a.site_id = ab.SIte_ID
        left JOIN (SELECT tech, SIte_ID,GROUP_CONCAT(Power_set ORDER BY grouping2 ASC SEPARATOR  "|")  AS powerU9 FROM isat_report.susy_sitelist_antltx_alltech_power_sec WHERE tech = 'U900' GROUP BY SIte_ID,tech ) ac On a.site_id = ac.SIte_ID
        left JOIN (SELECT tech, SIte_ID,GROUP_CONCAT(Power_set ORDER BY grouping2 ASC SEPARATOR  "|")  AS powerU21 FROM isat_report.susy_sitelist_antltx_alltech_power_sec WHERE tech = 'U2100' GROUP BY SIte_ID,tech ) ad On a.site_id = ad.SIte_ID
        left JOIN (SELECT tech, SIte_ID,GROUP_CONCAT(Power_set ORDER BY grouping2 ASC SEPARATOR  "|")  AS powerL9 FROM isat_report.susy_sitelist_antltx_alltech_power_sec WHERE tech = 'L900' GROUP BY SIte_ID,tech ) ae On a.site_id = ae.SIte_ID
        left JOIN (SELECT tech, SIte_ID,GROUP_CONCAT(Power_set ORDER BY grouping2 ASC SEPARATOR  "|")  AS powerL18 FROM isat_report.susy_sitelist_antltx_alltech_power_sec WHERE tech = 'L1800' GROUP BY SIte_ID,tech ) af On a.site_id= af.SIte_ID
        left JOIN (SELECT tech, SIte_ID,GROUP_CONCAT(Power_set ORDER BY grouping2 ASC SEPARATOR  "|")  AS powerL21 FROM isat_report.susy_sitelist_antltx_alltech_power_sec WHERE tech = 'L2100' GROUP BY SIte_ID,tech ) ag On a.site_id = ag.SIte_ID
        WHERE a.site_id <> "";
        """
    elif Request == "pwi_file_module2" :
        sqlscript_query = """
        Drop table if EXISTS isat_report.tempsmod2;
        Drop table if EXISTS isat_report.tempbbmod2;
        Drop table if EXISTS isat_report.temptrmod2;
        Drop table if EXISTS isat_report.susy_sitelist_antltx_alltech_power_sec;
        Drop table if EXISTS isat_report.susy_sitelist_antltx_alltech_power_sec2;
        """

    elif Request == "RET_ANGLE":
        sqlscript_query="""
        SELECT
        a.xdate
        , a.distName
        ,a.ald
        , a.MRBTS
        , a.sectorID
        , a.angle
        , a.maxAngle
        from isat_cm.retu a
        """
    elif Request == "4Gbw":
            sqlscript_query = """
            Drop table if EXISTS isat_report.BW900;
            create TABLE isat_report.BW900 (`SITE_ID` CHAR(50) NOT NULL,
            	`mrbts` INT(11) NOT NULL,
            	`lncel` INT(5) NOT NULL,
            	`BW900` VARCHAR(50) NULL DEFAULT NULL,
            	`administrativeState900` VARCHAR(50) NULL DEFAULT NULL,
            	`RemarkHos900` VARCHAR(50) NULL DEFAULT NULL,
            	PRIMARY KEY (SITE_ID,mrbts,lncel))
            SELECT Site_id_susy as SITE_ID,mrbts,lncel,GROUP_CONCAT(BW SEPARATOR "_") as BW900,GROUP_CONCAT(administrativeState SEPARATOR "_") as administrativeState900
            ,if(( INSTR(NAME,'_A1') or INSTR(NAME,'_A2') or INSTR(NAME,'_A3') or INSTR(NAME,'_B1') or INSTR(NAME,'_B2') or INSTR(NAME,'_B3') or INSTR(NAME,'_A4') or INSTR(NAME,'_A5') or INSTR(NAME,'_A6') or INSTR(NAME,'_B4') or INSTR(NAME,'_B5') or INSTR(NAME,'_B6'))<>0 ,"HOS","n") as RemarkHos900
				FROM isat_report.susy_profile4G  WHERE Band = 900 GROUP BY Site_id_susy,mrbts,lncel;

            Drop table if EXISTS isat_report.BW1800;
                    create TABLE isat_report.BW1800 (`SITE_ID` CHAR(50) NOT NULL,
                    	`mrbts` INT(11) NOT NULL,
                    	`lncel` INT(5) NOT NULL,
                    	`BW1800` VARCHAR(50) NULL DEFAULT NULL,
                    	`administrativeState1800` VARCHAR(50) NULL DEFAULT NULL,
                    	`RemarkHos1800` VARCHAR(50) NULL DEFAULT NULL,
                    	PRIMARY KEY (SITE_ID,mrbts,lncel))
            SELECT Site_id_susy as SITE_ID,mrbts,lncel,GROUP_CONCAT(BW SEPARATOR "_") as BW1800,GROUP_CONCAT(administrativeState SEPARATOR "_") as administrativeState1800
				,if(( INSTR(NAME,'_A1') or INSTR(NAME,'_A2') or INSTR(NAME,'_A3') or INSTR(NAME,'_B1') or INSTR(NAME,'_B2') or INSTR(NAME,'_B3') or INSTR(NAME,'_A4') or INSTR(NAME,'_A5') or INSTR(NAME,'_A6') or INSTR(NAME,'_B4') or INSTR(NAME,'_B5') or INSTR(NAME,'_B6'))<>0 ,"HOS","n") as RemarkHos1800
				FROM isat_report.susy_profile4G WHERE Band = 1800 GROUP BY Site_id_susy,mrbts,lncel;

            Drop table if EXISTS isat_report.BW2100;
                    create TABLE isat_report.BW2100 (`SITE_ID` CHAR(50) NOT NULL,
                    	`mrbts` INT(11) NOT NULL,
                    	`lncel` INT(5) NOT NULL,
                    	`BW2100` VARCHAR(50) NULL DEFAULT NULL,
                    	`administrativeState2100` VARCHAR(50) NULL DEFAULT NULL,
                    	`RemarkHos2100` VARCHAR(50) NULL DEFAULT NULL,
                    	PRIMARY KEY (SITE_ID,mrbts,lncel))
            SELECT Site_id_susy as SITE_ID,mrbts,lncel,GROUP_CONCAT(BW SEPARATOR "_") as BW2100,GROUP_CONCAT(administrativeState SEPARATOR "_") as administrativeState2100
				,if(( INSTR(NAME,'_A1') or INSTR(NAME,'_A2') or INSTR(NAME,'_A3') or INSTR(NAME,'_B1') or INSTR(NAME,'_B2') or INSTR(NAME,'_B3') or INSTR(NAME,'_A4') or INSTR(NAME,'_A5') or INSTR(NAME,'_A6') or INSTR(NAME,'_B4') or INSTR(NAME,'_B5') or INSTR(NAME,'_B6'))<>0 ,"HOS","n") as RemarkHos2100
				FROM isat_report.susy_profile4G WHERE Band = 2100 GROUP BY Site_id_susy,mrbts,lncel;

            Drop table if EXISTS isat_report.susy_BW4G;
                    create TABLE isat_report.susy_BW4G (`SITE_ID` CHAR(50) NOT NULL,
                    	`BW900` VARCHAR(50) NULL DEFAULT NULL,
                    	`BW1800` VARCHAR(50) NULL DEFAULT NULL,
                    	`BW2100` VARCHAR(50) NULL DEFAULT NULL,
                    	`administrativeState900` VARCHAR(50) NULL DEFAULT NULL,
                    	`administrativeState1800` VARCHAR(50) NULL DEFAULT NULL,
                    	`administrativeState2100` VARCHAR(50) NULL DEFAULT NULL,
                    	`countmrbts900` VARCHAR(50) NULL DEFAULT NULL,
                    	`countmrbts1800` VARCHAR(50) NULL DEFAULT NULL,
                    	`countmrbts2100` VARCHAR(50) NULL DEFAULT NULL,
                    	`RemarkHos900` VARCHAR(50) NULL DEFAULT NULL,
                    	`RemarkHos1800` VARCHAR(50) NULL DEFAULT NULL,
                    	`RemarkHos2100` VARCHAR(50) NULL DEFAULT NULL,
                    	PRIMARY KEY (SITE_ID))
            SELECT
                        a.SITE_ID
				, if(bc.BW900 is NULL,concat(ifnull(concat(b.BW900,"_"),""),ifnull(ba.BW900,"")),concat(ifnull(concat(b.BW900,"_"),""),ifnull(concat(ba.BW900,"_"),""),ifnull(bc.BW900,""))) AS BW900
				,if(cc.BW1800 is NULL,concat(ifnull(concat(c.BW1800,"_"),""),ifnull(ca.BW1800,"")), concat(ifnull(concat(c.BW1800,"_"),""),ifnull(concat(ca.BW1800,"_"),""),ifnull(cc.BW1800,""))) AS BW1800
				, if (dc.BW2100 is NULL,concat(ifnull(concat(d.BW2100,"_"),""),ifnull(da.BW2100,"")),concat(ifnull(concat(d.BW2100,"_"),""),ifnull(concat(da.BW2100,"_"),""),ifnull(dc.BW2100,""))) AS BW2100

				,if(bc.administrativeState900 is NULL,concat(ifnull(concat(b.administrativeState900,"_"),""),ifnull(ba.administrativeState900,"")),concat(ifnull(concat(b.administrativeState900,"_"),""),ifnull(concat(ba.administrativeState900,"_"),""),ifnull(bc.administrativeState900,""))) AS administrativeState900
				,if(cc.administrativeState1800 is NULL,concat(ifnull(concat(c.administrativeState1800,"_"),""),ifnull(ca.administrativeState1800,"")),concat(ifnull(concat(c.administrativeState1800,"_"),""),ifnull(concat(ca.administrativeState1800,"_"),""),ifnull(cc.administrativeState1800,""))) AS administrativeState1800
				, if(dc.administrativeState2100 is NULL,concat(ifnull(concat(d.administrativeState2100,"_"),""),ifnull(da.administrativeState2100,"")),concat(ifnull(concat(d.administrativeState2100,"_"),""),ifnull(concat(da.administrativeState2100,"_"),""),ifnull(dc.administrativeState2100,""))) AS administrativeState2100

				,if ( bc.countmrbts is NULL,concat(ifnull(concat(b.countmrbts,"_"),""),ifnull(ba.countmrbts,"")),concat(ifnull(concat(b.countmrbts,"_"),""),ifnull(concat(ba.countmrbts,"_"),""),ifnull(bc.countmrbts,""))) AS countmrbts900
				,if (cc.countmrbts is NULL,concat(ifnull(concat(c.countmrbts,"_"),""),ifnull(ca.countmrbts,"")),concat(ifnull(concat(c.countmrbts,"_"),""),ifnull(concat(ca.countmrbts,"_"),""),ifnull(cc.countmrbts,""))) AS countmrbts1800
				,if(dc.countmrbts is NULL,concat(ifnull(concat(d.countmrbts,"_"),""),ifnull(da.countmrbts,"")), concat(ifnull(concat(d.countmrbts,"_"),""),ifnull(concat(da.countmrbts,"_"),""),ifnull(dc.countmrbts,""))) AS countmrbts2100

				,if(bc.RemarkHos900 is NULL,concat(ifnull(concat(b.RemarkHos900,"_"),""),ifnull(ba.RemarkHos900,"")),concat(ifnull(concat(b.RemarkHos900,"_"),""),ifnull(concat(ba.RemarkHos900,"_"),""),ifnull(bc.RemarkHos900,""))) AS RemarkHos900
				,if(cc.RemarkHos1800 is NULL,concat(ifnull(concat(c.RemarkHos1800,"_"),""),ifnull(ca.RemarkHos1800,"")),concat(ifnull(concat(c.RemarkHos1800,"_"),""),ifnull(concat(ca.RemarkHos1800,"_"),""),ifnull(cc.RemarkHos1800,""))) AS RemarkHos1800
				,if(dc.RemarkHos2100 is NULL,concat(ifnull(concat(d.RemarkHos2100,"_"),""),ifnull(da.RemarkHos2100,"")), concat(ifnull(concat(d.RemarkHos2100,"_"),""),ifnull(concat(da.RemarkHos2100,"_"),""),ifnull(dc.RemarkHos2100,""))) AS RemarkHos2100


            FROM
            isat_report.susysiteidlist a
            LEFT JOIN
            (select SITE_ID,mrbts, GROUP_CONCAT( BW900 SEPARATOR ",") BW900,GROUP_CONCAT(administrativeState900 SEPARATOR ",") as administrativeState900 ,COUNT(DISTINCT  mrbts) as countmrbts,GROUP_CONCAT(RemarkHos900 SEPARATOR ",")  AS RemarkHos900 From isat_report.BW900 WHERE lncel IN (1,4,7,11) group by  SITE_ID ) b ON a.SITE_ID = b.SITE_ID #sector 1
            LEFT JOIN
				(select SITE_ID,mrbts, GROUP_CONCAT( BW900 SEPARATOR ",") BW900,GROUP_CONCAT(administrativeState900 SEPARATOR ",") as administrativeState900,COUNT(DISTINCT  mrbts) as countmrbts  ,GROUP_CONCAT(RemarkHos900 SEPARATOR ",")  AS RemarkHos900 From isat_report.BW900 WHERE lncel IN (2,5,8,12) group by  SITE_ID ) ba ON a.SITE_ID = ba.SITE_ID #sector 2
            LEFT JOIN
				(select SITE_ID,mrbts, GROUP_CONCAT( BW900 SEPARATOR ",") BW900,GROUP_CONCAT(administrativeState900 SEPARATOR ",") as administrativeState900,COUNT(DISTINCT  mrbts) as countmrbts ,GROUP_CONCAT(RemarkHos900 SEPARATOR ",")  AS RemarkHos900 From isat_report.BW900 WHERE lncel IN (3,6,9,13) group by  SITE_ID ) bc ON a.SITE_ID = bc.SITE_ID #sector 3
            LEFT Join
            (select SITE_ID, GROUP_CONCAT( BW1800 SEPARATOR ",") BW1800,GROUP_CONCAT(administrativeState1800 SEPARATOR ",") as administrativeState1800,COUNT(DISTINCT  mrbts) as countmrbts,GROUP_CONCAT(RemarkHos1800 SEPARATOR ",")  AS RemarkHos1800   From isat_report.BW1800 WHERE lncel IN (1,4,7,11) group by  SITE_ID ) c ON a.SITE_ID = c.SITE_ID #sector 1
            LEFT Join
            (select SITE_ID, GROUP_CONCAT( BW1800 SEPARATOR ",") BW1800,GROUP_CONCAT(administrativeState1800 SEPARATOR ",") as administrativeState1800 ,COUNT(DISTINCT  mrbts) as countmrbts,GROUP_CONCAT(RemarkHos1800 SEPARATOR ",")  AS RemarkHos1800  From isat_report.BW1800 WHERE lncel IN (2,5,8,12) group by  SITE_ID ) ca ON a.SITE_ID = ca.SITE_ID #sector 2
            LEFT Join
            (select SITE_ID, GROUP_CONCAT( BW1800 SEPARATOR ",") BW1800,GROUP_CONCAT(administrativeState1800 SEPARATOR ",") as administrativeState1800 ,COUNT(DISTINCT  mrbts) as countmrbts,GROUP_CONCAT(RemarkHos1800 SEPARATOR ",")  AS RemarkHos1800  From isat_report.BW1800 WHERE lncel IN (3,6,9,13) group by  SITE_ID ) cc ON a.SITE_ID = cc.SITE_ID #sector 3
            LEFT Join
            (select SITE_ID, GROUP_CONCAT( BW2100 SEPARATOR ",") BW2100,GROUP_CONCAT(administrativeState2100 SEPARATOR ",") as administrativeState2100 ,COUNT(DISTINCT  mrbts) as countmrbts,GROUP_CONCAT(RemarkHos2100 SEPARATOR ",")  AS RemarkHos2100  From isat_report.BW2100 WHERE lncel IN (1,4,7,11) group by  SITE_ID ) d ON a.SITE_ID = d.SITE_ID #sector 1
            LEFT Join
            (select SITE_ID, GROUP_CONCAT( BW2100 SEPARATOR ",") BW2100,GROUP_CONCAT(administrativeState2100 SEPARATOR ",") as administrativeState2100 ,COUNT(DISTINCT  mrbts) as countmrbts,GROUP_CONCAT(RemarkHos2100 SEPARATOR ",")  AS RemarkHos2100  From isat_report.BW2100 WHERE lncel IN (2,5,8,12) group by  SITE_ID ) da ON a.SITE_ID = da.SITE_ID #sector 2
            LEFT Join
            (select SITE_ID, GROUP_CONCAT( BW2100 SEPARATOR ",") BW2100,GROUP_CONCAT(administrativeState2100 SEPARATOR ",") as administrativeState2100  ,COUNT(DISTINCT  mrbts) as countmrbts,GROUP_CONCAT(RemarkHos2100 SEPARATOR ",")  AS RemarkHos2100  From isat_report.BW2100 WHERE lncel IN (3,6,9,13) group by  SITE_ID ) dc ON a.SITE_ID = dc.SITE_ID #sector 3

            GROUP BY  a.SITE_ID;

            Drop table if EXISTS isat_report.BW900;
            Drop table if EXISTS isat_report.BW1800;
            Drop table if EXISTS isat_report.BW2100"""
    elif Request == "site_id_reference":
        sqlscript_query = """
        DROP TABLE if EXISTS isat_report.ndbonline;
        CREATE TABLE isat_report.ndbonline
        		 (`siteid` CHAR(50) NOT NULL,
         	`cellid` INT(11) NOT NULL,
         	`RNCBSC` INT(10) DEFAULT 0,
         	`tech` CHAR(10) NOT NULL,
				`SectorID` INT(10) DEFAULT 0, PRIMARY KEY (siteid,cellid,RNCBSC))
        SELECT a.`SITE ID` AS siteid,a.`CELL ID` AS cellid,if(a.`BSC/RNC ID` = "",0,a.`BSC/RNC ID`) AS RNCBSC,
        LEFT(UnikID,2) AS tech,a.SectorID
        FROM isat_ndb.t_ndb_cell a
        GROUP BY a.`SITE ID`,a.`CELL ID`,a.`BSC/RNC ID`;
        DROP TABLE if EXISTS isat_report.temp_lncel;

        CREATE TABLE isat_report.temp_lncel
        		 (`mrbts` INT(11) NOT NULL,
         	`lncel` SMALLINT(5) NOT NULL,
         	`cellid` INT(11) NOT NULL, PRIMARY KEY (cellid))
        SELECT a.mrbts,a.lnCel, CONCAT(mrbts,lnCel) AS cellid
        FROM isat_cm.lncel_fdd a
        WHERE xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """'
        GROUP BY a.mrbts,a.lnCel;
        DROP TABLE if EXISTS isat_report.list_lncel_temp;

        CREATE TABLE isat_report.list_lncel_temp
        		 (`siteid` CHAR(50) NOT NULL,
         	`mrbts` INT(11) NOT NULL,
         	`lncel` SMALLINT(10) NOT NULL, PRIMARY KEY (siteid,mrbts,lncel))
        SELECT a.mrbts,a.lncel, CONCAT("Dummy_",a.mrbts) AS siteid
        FROM isat_report.temp_lncel a
        WHERE NOT a.cellid IN (
        SELECT a.cellid
        FROM isat_report.ndbonline a
        JOIN isat_report.temp_lncel b ON a.cellid = b.cellid
        WHERE tech = '4G') ;

        DROP TABLE if EXISTS isat_report.list_lncel_temp2;
        CREATE TABLE isat_report.list_lncel_temp2
        		 (`siteid` CHAR(50) NOT NULL,
         	`mrbts` INT(11) NOT NULL,
         	`lncel` SMALLINT(10) NOT NULL, PRIMARY KEY (siteid,mrbts,lncel))
        SELECT b.mrbts,b.lncel,a.siteid
        FROM isat_report.ndbonline a
        JOIN isat_report.temp_lncel b ON a.cellid = b.cellid
        WHERE tech = '4G' ;

        UPDATE isat_report.list_lncel_temp a, isat_report.list_lncel_temp2 b SET a.siteid = b.siteid
        WHERE a.mrbts= b.mrbts;

        DROP TABLE if EXISTS isat_report.list_lncel;
        CREATE TABLE isat_report.list_lncel
        		 (`siteid` CHAR(50) NOT NULL,
         	`mrbts` INT(11) NOT NULL,
         	`lncel` SMALLINT(10) NOT NULL, PRIMARY KEY (siteid,mrbts,lncel))
        (
        SELECT mrbts,lncel,siteid
        FROM isat_report.list_lncel_temp2) UNION(
        SELECT mrbts,lncel,siteid
        FROM isat_report.list_lncel_temp);
        DROP TABLE if EXISTS isat_report.list_lncel_temp2;
        DROP TABLE if EXISTS isat_report.list_lncel_temp;
        DROP TABLE if EXISTS isat_report.temp_lncel;



        Drop table if EXISTS isat_report.temp_wcel;
                create TABLE isat_report.temp_wcel
        		  (`RNC` INT(11) NOT NULL,
                	`WBTS`  INT(11) NOT NULL,
                	`WCEL`  INT(11) NOT NULL,
                	PRIMARY KEY (RNC,WBTS,WCEL))
        SELECT RNC,WBTS,WCEL FROM isat_cm.wcel a WHERE xdate =    '""" + hwitime.strftime("%Y-%m-%d") + """'    GROUP BY RNC,WBTS,WCEL;

        Drop table if EXISTS isat_report.list_wcel_temp;
                create TABLE isat_report.list_wcel_temp
        		  (`RNC` INT(11) NOT NULL,
                	`WBTS`  INT(11) NOT NULL,
                	`WCEL`  INT(11) NOT NULL,
                	`siteid` CHAR(50) NOT NULL,
                	PRIMARY KEY (RNC,WBTS,WCEL))
        SELECT a.RNC,a.WBTS,a.WCEL,CONCAT("Dummy_",a.RNC,a.WBTS) as siteid
        FROM isat_report.temp_wcel a
        WHERE NOT concat(a.RNC,a.WCEL) IN (
        SELECT concat(a.RNC,a.WCEL)
        FROM isat_report.temp_wcel a
        JOIN isat_report.ndbonline b ON a.rnc = b.RNCBSC AND a.WCEL = b.cellid
        WHERE tech = '3G') ;

        Drop table if EXISTS isat_report.list_wcel_temp2;
                create TABLE isat_report.list_wcel_temp2
        		  (`RNC` INT(11) NOT NULL,
                	`WBTS`  INT(11) NOT NULL,
                	`WCEL`  INT(11) NOT NULL,
                	`siteid` CHAR(50) NOT NULL,
                	PRIMARY KEY (RNC,WBTS,WCEL))
        SELECT a.RNC,a.WBTS,a.WCEL,b.siteid FROM isat_report.temp_wcel a JOIN isat_report.ndbonline b ON a.rnc = b.RNCBSC AND a.WCEL = b.cellid WHERE tech = '3G' GROUP BY RNC,WBTS,WCEL;

        UPDATE isat_report.list_wcel_temp a, isat_report.list_wcel_temp2 b SET a.siteid = b.siteid
        WHERE a.RNC= b.RNC AND a.WBTS = b.WBTS;

        Drop table if EXISTS isat_report.list_wcel;
                create TABLE isat_report.list_wcel
        		  (`RNC` INT(11) NOT NULL,
                	`WBTS`  INT(11) NOT NULL,
                	`WCEL`  INT(11) NOT NULL,
                	`siteid` CHAR(50) NOT NULL,
                	PRIMARY KEY (RNC,WBTS,WCEL))
        (SELECT a.RNC,a.WBTS,a.WCEL,a.siteid FROM isat_report.list_wcel_temp2 a )
        UNION
        (
        SELECT a.RNC,a.WBTS,a.WCEL, siteid
        FROM isat_report.list_wcel_temp a );
        Drop table if EXISTS isat_report.list_wcel_temp2;
        Drop table if EXISTS isat_report.list_wcel_temp;
        Drop table if EXISTS isat_report.temp_wcel;


         Drop table if EXISTS isat_report.temp_bts;
                create TABLE isat_report.temp_bts
        		  (`BSC` INT(11) NOT NULL,
                	`BCF`  INT(11) NOT NULL,
                	`BTS`  INT(11) NOT NULL,
                	`cellid`  INT(11) default 0,
                	`SectorID`  INT(11) default 0,
                	PRIMARY KEY (BSC,BCF,BTS,cellid))
        SELECT BSC,BCF,bts,a.cellId,SectorID FROM isat_cm.bts a WHERE xdate =     '""" + hwitime.strftime("%Y-%m-%d") + """'    GROUP BY BSC,BCF,BTS,cellId;

        Drop table if EXISTS isat_report.list_bts_temp;
                create TABLE isat_report.list_bts_temp
        		  (`BSC` INT(11) NOT NULL,
                	`BCF`  INT(11) NOT NULL,
                	`BTS`  INT(11) NOT NULL,
                	`cellid`  INT(11) NOT NULL,
                	`siteid` CHAR(50) NOT NULL,
                	`SectorID`  INT(11) NOT NULL,
                	PRIMARY KEY (BSC,BCF,BTS))
        SELECT a.BSC,a.BCF,a.BTS,b.siteid,b.cellid,b.SectorID FROM isat_report.temp_bts a JOIN isat_report.ndbonline b ON a.BSC = b.RNCBSC AND a.cellid = b.cellid WHERE tech = '2G' GROUP BY BSC,BCF,BTS;

        Drop table if EXISTS isat_report.list_bts_temp2;
                create TABLE isat_report.list_bts_temp2
        		  (`BSC` INT(11) NOT NULL,
                	`BCF`  INT(11) NOT NULL,
                	`BTS`  INT(11) NOT NULL,
                    `cellid`  INT(11) default 0,
                	`siteid` CHAR(50) NOT NULL,
                	`SectorID`  INT(11) NOT NULL,
                	PRIMARY KEY (BSC,BCF,BTS))
        SELECT a.BSC,a.BCF,a.BTS,cellid,CONCAT("Dummy_",a.BSC,a.BCF) as siteid,a.SectorID
        FROM isat_report.temp_bts a
        WHERE NOT concat(a.BSC,a.cellid) IN (SELECT concat(a.BSC,a.cellid)
        FROM isat_report.temp_bts a JOIN isat_report.ndbonline b ON a.BSC = b.RNCBSC AND a.cellid = b.cellid WHERE tech = '2G' GROUP BY BSC,BCF,BTS) ;

        UPDATE isat_report.list_bts_temp a, isat_report.list_bts_temp2 b SET a.siteid = b.siteid
        WHERE a.BSC= b.BSC AND a.BCF = b.BCF;

        Drop table if EXISTS isat_report.list_bts;
                create TABLE isat_report.list_bts
        		  (`bscid` INT(11) NOT NULL,
                	`bcfid`  INT(11) NOT NULL,
                	`btsid`  INT(11) NOT NULL,
                    `cellid`  INT(11) default 0,
                	`siteid` CHAR(50) NOT NULL,
                	`SectorID`  INT(11) NOT NULL,
                	PRIMARY KEY (bscid,bcfid,btsid,cellid))
        (SELECT a.BSC AS bscid,a.BCF AS bcfid,a.BTS AS btsid,cellid,a.siteid,SectorID FROM isat_report.list_bts_temp2 a )
        UNION
        (
        SELECT a.BSC AS bscid,a.BCF AS bcfid,a.BTS AS btsid,cellid, siteid,SectorID
        FROM isat_report.list_bts_temp a
        );

        Drop table if EXISTS isat_report.list_bts_temp2;
        Drop table if EXISTS isat_report.list_bts_temp;
        Drop table if EXISTS isat_report.temp_bts;
        DROP TABLE if EXISTS isat_report.ndbonline;
        """
    elif Request == "hwi_profile2G":
        sqlscript_query = """
        Drop table if EXISTS isat_report.susy_profile2G_macro;
        create TABLE isat_report.susy_profile2G_macro(`oss` CHAR(10) NULL DEFAULT NULL,
		  `SITE_ID` CHAR(50) NULL DEFAULT NULL,
        	`bsc` INT(11) NULL DEFAULT NULL,
        	`bcf` SMALLINT(5) NULL DEFAULT NULL,
        	`bts` SMALLINT(5) NULL DEFAULT NULL,
        	`cellId` INT(11) NULL DEFAULT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`bcf_susy` SMALLINT(5) NULL DEFAULT NULL,
        	`BAND` CHAR(50) NULL DEFAULT NULL,
        	`Sector_ID` SMALLINT(5) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`adminState` SMALLINT(5) NULL DEFAULT NULL,
        	PRIMARY KEY (bsc,bcf,bts,cellId))
        SELECT a.oss,b.siteid as SITE_ID,a.bsc,a.bcf,a.bts,a.cellId,NAME,if(LEFT(NAME,1)="_",CONCAT(b.SITEID,"_IBS"),b.SITEID) AS Site_id_susy,a.bts AS bcf_susy,if (a.frequencybandinuse = 0 , 900,1800) as BAND,b.sectorid AS Sector_ID, if(LEFT(NAME,1)="_","INDOOR","MACRO") AS Remark,a.adminState
        FROM isat_cm.bts a JOIN isat_report.list_bts b ON a.bsc = b.bscid AND a.BCF = b.bcfid AND a.BTS = b.btsid AND a.cellId = b.cellId
        WHERE xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.SITEID <> "" and LEFT(NAME,1)<>"_"GROUP BY a.bsc,a.bcf,a.bts;

        Drop table if EXISTS isat_report.susy_profile2G_ibs;
        create TABLE isat_report.susy_profile2G_ibs(`oss` CHAR(10) NULL DEFAULT NULL,
		  `SITE_ID` CHAR(50) NULL DEFAULT NULL,
        	`bsc` INT(11) NULL DEFAULT NULL,
        	`bcf` SMALLINT(5) NULL DEFAULT NULL,
        	`bts` SMALLINT(5) NULL DEFAULT NULL,
        	`cellId` INT(11) NULL DEFAULT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`bcf_susy` SMALLINT(5) NULL DEFAULT NULL,
        	`BAND` CHAR(50) NULL DEFAULT NULL,
        	`Sector_ID` SMALLINT(5) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`adminState` SMALLINT(5) NULL DEFAULT NULL,
        	PRIMARY KEY (bsc,bcf,bts))
        SELECT a.oss,b.siteid as SITE_ID,a.bsc,a.bcf,a.bts,a.cellId,NAME,if(LEFT(NAME,1)="_",CONCAT(b.SITEID,"_IBS"),b.SITEID) AS Site_id_susy,a.bts AS bcf_susy,if (a.frequencybandinuse = 0 , 900,1800) as BAND,b.sectorid AS Sector_ID, if(LEFT(NAME,1)="_","INDOOR","MACRO") AS Remark,a.adminState
        FROM isat_cm.bts a JOIN isat_report.list_bts b ON a.bsc = b.bscid AND a.BCF = b.bcfid AND a.BTS = b.btsid AND a.cellId = b.cellId
        WHERE xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.SITEID <> "" and LEFT(NAME,1)="_"GROUP BY a.bsc,a.bcf,a.bts;



        Drop table if EXISTS isat_report.susy_profile2G_temp;
        create TABLE isat_report.susy_profile2G_temp(`oss` CHAR(10) NULL DEFAULT NULL,
		  `SITE_ID` CHAR(50) NULL DEFAULT NULL,
        	`bsc` INT(11) NULL DEFAULT NULL,
        	`bcf` SMALLINT(5) NULL DEFAULT NULL,
        	`bts` SMALLINT(5) NULL DEFAULT NULL,
        	`cellId` INT(11) NULL DEFAULT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`bcf_susy` SMALLINT(5) NULL DEFAULT NULL,
        	`BAND` CHAR(50) NULL DEFAULT NULL,
        	`Sector_ID` SMALLINT(5) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`adminState` SMALLINT(5) NULL DEFAULT NULL,
        	PRIMARY KEY (bsc,bcf,bts))
        (SELECT oss,SITE_ID,bsc,bcf,bts,cellId,NAME,Site_id_susy, bcf_susy,Band,Sector_ID, Remark,adminState
        FROM isat_report.susy_profile2G_macro GROUP BY bsc,bcf,bts)
        UNION
        (SELECT b.oss,b.SITE_ID,b.bsc,b.bcf,b.bts,b.cellId,b.NAME,b.Site_id_susy, 0  as bcf_susy,b.Band,b.Sector_ID, b.Remark,b.adminState
        FROM isat_report.susy_profile2G_macro a
        JOIN  isat_report.susy_profile2G_ibs b ON a.SITE_ID = b.SITE_ID AND a.bsc = b.bsc AND a.bcf = b.bcf GROUP BY b.bsc,b.bcf,b.bts)
        UNION
        (SELECT b.oss,b.SITE_ID,b.bsc,b.bcf,b.bts,b.cellId,b.NAME,b.Site_id_susy, b.bcf_susy,b.Band,b.Sector_ID,b.Remark,b.adminState
        FROM isat_report.susy_profile2G_macro a
        right JOIN  isat_report.susy_profile2G_ibs b ON a.SITE_ID = b.SITE_ID AND a.bsc = b.bsc AND a.bcf = b.bcf where a.bcf is null GROUP BY  b.bsc,b.bcf,b.bts)
        UNION
        (SELECT a.oss,b.siteid as SITE_ID,a.bsc,a.bcf,a.bts,a.cellId,a.NAME,if(LEFT(a.NAME,1)="_",CONCAT(b.siteid,"_IBS"),b.siteid) AS Site_id_susy,a.bts AS bcf_susy,if(a.frequencybandinuse = 0 , 900,1800) as BAND,b.sectorid AS Sector_ID, if(LEFT(a.NAME,1)="_","INDOOR","MACRO") AS Remark,a.adminState
        FROM isat_cm.bts a JOIN isat_report.list_bts b ON a.bsc = b.bscid AND a.BCF = b.bcfid AND a.BTS = b.btsid AND a.cellId = b.cellId
        left JOIN isat_report.susy_profile2G_macro c ON a.bsc = c.bsc AND a.BCF = c.BCF AND a.BTS = c.BTS
        WHERE xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.siteid <> "" AND a.NAME IS NULL AND c.bcf IS null GROUP BY a.bsc,a.bcf,a.bts);

        Drop table if EXISTS isat_report.temp_mrbts2g;
        create TABLE isat_report.temp_mrbts2g (
            `BSC` INT(11) NOT NULL,
            `BCF` INT(11) NOT NULL,
            `version` CHAR(50) NOT NULL,
            PRIMARY KEY (BSC,BCF))
            SELECT BSC,BCF,version
               FROM isat_cm.mrbts WHERE xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """'  AND bsc IS NOT null GROUP BY bsc,bcf;



        Drop table if EXISTS isat_report.susy_profile2G;
        create TABLE isat_report.susy_profile2G(`oss` CHAR(10) NULL DEFAULT NULL,
		  `SITE_ID` CHAR(50) NULL DEFAULT NULL,
        	`bsc` INT(11) NOT NULL,
        	`bcf` SMALLINT(5) NOT NULL,
        	`bts` SMALLINT(5) NOT NULL,
        	`cellId` INT(11) NULL DEFAULT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`bcf_susy` SMALLINT(5) NULL DEFAULT NULL,
        	`BAND` CHAR(50) NULL DEFAULT NULL,
        	`Sector_ID` SMALLINT(5) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`adminState` SMALLINT(5) NULL DEFAULT NULL,
        	`SBTSID` CHAR(50) DEFAULT 0,
        	`SBTS_status` CHAR(50) NULL DEFAULT NULL,
        	`Site_id_2G` VARCHAR(54) NULL DEFAULT NULL,
        	PRIMARY KEY (bsc,bcf,bts,SBTSID))
        (SELECT a.oss, a.SITE_ID,a.bsc,a.bcf,a.bts,a.cellId,a.NAME,if(c.site_id is null,a.Site_id_susy,c.site_id) AS Site_id_susy , a.bcf_susy,a.Band,a.Sector_ID, a.Remark,a.adminState,ifnull(b.SBTSId,0) AS SBTSId,c.version AS SBTS_status,if(c.site_id = a.Site_id_susy,NULL,a.Site_id_susy) AS Site_id_2G
        FROM isat_report.susy_profile2G_temp a
		  JOIN isat_cm.bcf b ON a.bsc = b.bsc AND a.bcf = b.BCF
		  LEFT JOIN (SELECT mrbts,site_id,version FROM isat_report.susy_profile4g GROUP BY mrbts,site_id) c ON b.SBTSId = c.mrbts
        WHERE b.xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.SBTSId IS NOT null group BY bsc,bcf,bts)

        UNION

        (SELECT a.oss,a.SITE_ID,a.bsc,a.bcf,a.bts,a.cellId,a.NAME,a.Site_id_susy, a.bcf_susy,a.Band,a.Sector_ID, a.Remark,a.adminState,ifnull(b.SBTSId,0) AS SBTSId,
		  c.version AS SBTS_status,
		  NULL AS Site_id_2G
        FROM isat_report.susy_profile2G_temp a
        JOIN isat_cm.bcf b ON a.bsc = b.bsc AND a.bcf = b.BCF
        LEFT JOIN isat_report.temp_mrbts2g c On a.bsc = c.bsc AND a.bcf = c.BCF
        WHERE b.xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.SBTSId IS null group BY bsc,bcf,bts);

        Drop table if EXISTS isat_report.susy_profile2G_macro;
        Drop table if EXISTS isat_report.susy_profile2G_ibs;
        Drop table if EXISTS isat_report.susy_profile2G_temp;
        Drop table if EXISTS isat_report.temp_mrbts2g;
        """
    elif Request == "hwi_profile3G":
        sqlscript_query = """
        Drop table if EXISTS isat_report.susy_profile3G_macro;
        create TABLE isat_report.susy_profile3G_macro(`oss` VARCHAR(10) NULL DEFAULT NULL,
		  `SITE_ID` CHAR(50) NULL DEFAULT NULL,
        	`RNC` SMALLINT(6) NOT NULL,
        	`WBTS` SMALLINT(6) NOT NULL,
        	`WCEL` INT(11) NOT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`WBTS_susy` SMALLINT(6) NULL DEFAULT NULL,
        	`Band` CHAR(50) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`AdminCellState` SMALLINT(6) NULL DEFAULT NULL,
        	PRIMARY KEY (RNC,WBTS,WCEL))
        SELECT a.oss,b.siteid as SITE_ID,a.RNC,a.WBTS,a.WCEL,NAME,if(LEFT(NAME,1)="_",CONCAT(b.SITEID,"_IBS"),b.SITEID) AS Site_id_susy,a.WBTS as WBTS_susy, if (a.UARFCN = 3013,900,2100) as Band, if(LEFT(NAME,1)="_","INDOOR","MACRO") AS Remark,a.AdminCellState
        FROM isat_cm.wcel a JOIN isat_report.list_wcel b ON a.RNC = b.RNC AND a.WBTS = b.WBTS AND a.WCEL = b.wcel
        WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.SITEID <> "" and LEFT(NAME,1)<>"_" GROUP BY a.RNC,a.WBTS,a.WCEL;

        Drop table if EXISTS isat_report.susy_profile3G_ibs;
        create TABLE isat_report.susy_profile3G_ibs(`oss` VARCHAR(10) NULL DEFAULT NULL,
		  `SITE_ID` CHAR(50) NULL DEFAULT NULL,
        	`RNC` SMALLINT(6) NOT NULL,
        	`WBTS` SMALLINT(6) NOT NULL,
        	`WCEL` INT(11) NOT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`WBTS_susy` SMALLINT(6) NULL DEFAULT NULL,
        	`Band` CHAR(50) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`AdminCellState` SMALLINT(6) NULL DEFAULT NULL,
        	PRIMARY KEY (RNC,WBTS,WCEL))
        SELECT a.oss,b.siteid as SITE_ID,a.RNC,a.WBTS,a.WCEL,NAME,if(LEFT(NAME,1)="_",CONCAT(b.SITEID,"_IBS"),b.SITEID) AS Site_id_susy,a.WBTS as WBTS_susy, if (a.UARFCN = 3013,900,2100) as Band, if(LEFT(NAME,1)="_","INDOOR","MACRO") AS Remark,a.AdminCellState
        FROM isat_cm.wcel a JOIN isat_report.list_wcel b ON a.RNC = b.RNC AND a.WBTS = b.WBTS AND a.WCEL = b.wcel
        WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.SITEID <> "" and LEFT(NAME,1)="_" GROUP BY a.RNC,a.WBTS,a.WCEL;

        Drop table if EXISTS isat_report.temp_mrbts3G;
        create TABLE isat_report.temp_mrbts3G (
            `RNC` INT(11) NOT NULL,
            `WBTS` INT(11) NOT NULL,
            `version` CHAR(50) NOT NULL,
            PRIMARY KEY (RNC,WBTS))
            SELECT RNC,WBTS,version
               FROM isat_cm.mrbts WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'  AND RNC IS NOT null GROUP BY RNC,WBTS;

        Drop table if EXISTS isat_report.susy_profile3G_temp;
        create TABLE isat_report.susy_profile3G_temp(`oss` VARCHAR(10) NULL DEFAULT NULL,
		  `SITE_ID` CHAR(50) NULL DEFAULT NULL,
        	`RNC` SMALLINT(6) NOT NULL,
        	`WBTS` SMALLINT(6) NOT NULL,
        	`WCEL` INT(11) NOT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`WBTS_susy` SMALLINT(6) NULL DEFAULT NULL,
        	`Band` CHAR(50) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`AdminCellState` SMALLINT(6) NULL DEFAULT NULL,
        	PRIMARY KEY (RNC,WBTS,WCEL))
        (SELECT oss,SITE_ID,RNC,WBTS,WCEL,NAME,Site_id_susy, WBTS_susy,Band, Remark,AdminCellState
        FROM isat_report.susy_profile3G_macro GROUP BY RNC,WBTS,WCEL)
        UNION
        (SELECT b.oss,b.SITE_ID,b.RNC,b.WBTS,b.WCEL,b.NAME,b.Site_id_susy, 0  as WBTS_susy,b.Band, b.Remark,b.AdminCellState
        FROM isat_report.susy_profile3G_macro a
        JOIN  isat_report.susy_profile3G_ibs b ON a.SITE_ID = b.SITE_ID AND a.RNC = b.RNC AND a.WBTS = b.WBTS GROUP BY b.RNC,b.WBTS,b.WCEL)
        UNION
        (SELECT b.oss, b.SITE_ID,b.RNC,b.WBTS,b.WCEL,b.NAME,b.Site_id_susy, b.WBTS_susy,b.Band, b.Remark,b.AdminCellState
        FROM isat_report.susy_profile3G_macro a
        right JOIN  isat_report.susy_profile3G_ibs b ON a.SITE_ID = b.SITE_ID AND a.RNC = b.RNC AND a.WBTS = b.WBTS  where a.WBTS is null GROUP BY b.RNC,b.WBTS,b.WCEL)
        UNION
        (SELECT a.oss, b.SITEID AS SIte_id ,a.RNC,a.WBTS,a.WCEL,a.NAME,if(LEFT(a.NAME,1)="_",CONCAT(b.SITEID,"_IBS"),b.SITEID) AS Site_id_susy,a.WBTS as WBTS_susy, if (a.UARFCN = 3013,900,2100) as Band, if(LEFT(a.NAME,1)="_","INDOOR","MACRO") AS Remark,a.AdminCellState
        FROM isat_cm.wcel a JOIN isat_report.list_wcel b ON a.RNC = b.RNC AND a.WBTS = b.WBTS AND a.WCEL = b.wcel
        left JOIN isat_report.susy_profile3G_macro c ON a.RNC = c.RNC AND a.WBTS = c.WBTS AND a.WCEL = c.WCEL
        WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.SITEID <> "" AND a.name IS null AND c.WCEL IS NULL GROUP BY a.RNC,a.WBTS,a.WCEL);

        Drop table if EXISTS isat_report.susy_profile3G;
        create TABLE isat_report.susy_profile3G(`oss` VARCHAR(10) NULL DEFAULT NULL,
		  `SITE_ID` CHAR(50) NULL DEFAULT NULL,
        	`RNC` SMALLINT(6) NOT NULL,
        	`WBTS` SMALLINT(6) NOT NULL,
        	`WCEL` INT(11) NOT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`WBTS_susy` SMALLINT(6) NULL DEFAULT NULL,
        	`Band` CHAR(50) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`AdminCellState` SMALLINT(6) NULL DEFAULT NULL,
        	`SBTSID` CHAR(50) DEFAULT 0,
        	`SBTS_status` CHAR(50) NULL DEFAULT NULL,
        	`Site_id_3G` VARCHAR(54) NULL DEFAULT NULL,
        	PRIMARY KEY (RNC,WBTS,WCEL,SBTSID))
        (SELECT a.oss, a.site_id as SITE_ID,a.RNC,a.WBTS,a.WCEL,a.NAME,if(c.site_id is null,a.Site_id_susy,c.site_id) AS Site_id_susy, a.WBTS_susy,a.Band, a.Remark,a.AdminCellState,ifnull(b.SBTSId,0) AS SBTSId,c.version AS SBTS_status,if(c.site_id = a.Site_id_susy,NULL,a.Site_id_susy) AS Site_id_3G
        FROM isat_report.susy_profile3G_temp a
		  JOIN isat_cm.wbts b ON a.RNC = b.RNC AND a.WBTS = b.WBTS
		  LEFT JOIN (SELECT mrbts,Site_id_susy as site_id,version FROM isat_report.susy_profile4g GROUP BY mrbts,Site_id_susy) c ON b.SBTSId = c.mrbts
		  WHERE b.xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.SBTSId IS NOT null GROUP BY a.RNC,a.WBTS,a.WCEL)
        UNION
        (SELECT a.oss,a.SITE_ID,a.RNC,a.WBTS,a.WCEL,a.NAME,a.Site_id_susy, a.WBTS_susy,a.Band, a.Remark,a.AdminCellState,ifnull(b.SBTSId,0) AS SBTSId,d.version AS SBTS_status,NULL AS Site_id_3G
        FROM isat_report.susy_profile3G_temp a
        JOIN isat_cm.wbts b ON a.RNC = b.RNC AND a.WBTS = b.WBTS
        Left JOIN isat_report.susy_profile3G_temp c ON a.RNC = c.RNC AND a.WBTS = c.WBTS
        Left JOIN isat_report.temp_mrbts3G d ON a.RNC = d.RNC AND a.WBTS = d.WBTS
        WHERE b.xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """'  AND b.SBTSId IS null GROUP BY a.RNC,a.WBTS,a.WCEL);


        Drop table if EXISTS isat_report.susy_profile3G_macro;
        Drop table if EXISTS isat_report.susy_profile3G_ibs;
        Drop table if EXISTS isat_report.susy_profile3G_temp;
        Drop table if EXISTS isat_report.temp_mrbts3G;
        """
    elif Request == "hwi_profile4G":
        sqlscript_query = """
        Drop table if EXISTS isat_report.susy_temp_mrbtssiteid;
        create TABLE isat_report.susy_temp_mrbtssiteid
		  (`Site_id` VARCHAR(54) NOT NULL DEFAULT '',
		  `mrbts_id` INT(11) NOT NULL,
        	PRIMARY KEY (mrbts_id))
        SELECT siteid AS Site_id,mrbts AS mrbts_id
        FROM(
        SELECT b.siteid,b.mrbts
        FROM isat_cm.lncel a
        JOIN isat_report.list_lncel b ON a.MRBTS = b.mrbts AND a.LNCEL = b.lnCel
        WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' and LEFT(a.NAME,1)="_"  GROUP BY b.siteid,b.mrbts) a GROUP BY a.siteid;

        Drop table if EXISTS isat_report.susy_temp_mrbtssiteid_ibsid;
                create TABLE isat_report.susy_temp_mrbtssiteid_ibsid
        		  (`Site_id` VARCHAR(54) NOT NULL DEFAULT '',
        		  `mrbts_id` INT(11) NOT NULL,
        		  `Site_id_susy` VARCHAR(54) NOT NULL DEFAULT '',
                	PRIMARY KEY (mrbts_id))
        (SELECT a.siteid as site_id,a.mrbts as mrbts_id ,CONCAT(a.siteid,"_IBS2") AS Site_id_susy
        FROM(
        SELECT b.siteid,b.mrbts
        FROM isat_cm.lncel a
        JOIN isat_report.list_lncel  b ON a.MRBTS = b.mrbts AND a.LNCEL = b.lnCel
        WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' and LEFT(a.NAME,1)="_" GROUP BY b.siteid,b.mrbts) a
        LEFT JOIN isat_report.susy_temp_mrbtssiteid b ON a.mrbts = b.mrbts_id
        WHERE b.mrbts_id IS NULL)
        UNION
        (SELECT site_id,mrbts_id ,CONCAT(site_id,"_IBS") AS Site_id_susy FROM isat_report.susy_temp_mrbtssiteid );




        Drop table if EXISTS isat_report.temp_lncel_fdd;
        create TABLE isat_report.temp_lncel_fdd (
        `oss`VARCHAR(50) NULL DEFAULT NULL,
        	`mrbts` INT(11) NOT NULL,
        	`lncel` SMALLINT(5) NOT NULL,
        	`dlMimoMode` SMALLINT(5) NOT NULL,
        	`BAND` CHAR(50) NULL DEFAULT NULL,
        	`BW` DOUBLE(17,0) NULL DEFAULT NULL,
        	PRIMARY KEY (mrbts,lncel))
        	SELECT oss,mrbts,lncel,dlMimoMode
			  ,if(earfcnDL<1000,2100,if((earfcnDL>1000 and earfcnDL<3000),1800,900 )) AS BAND
			  ,ROUND(dlChBw/10,0)  AS BW
			   FROM isat_cm.lncel_fdd WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'  GROUP BY mrbts,lncel;

        Drop table if EXISTS isat_report.temp_mrbts;
        create TABLE isat_report.temp_mrbts (
        	`MRBTS` INT(11) NOT NULL,
        	`version` CHAR(50) NOT NULL,
        	PRIMARY KEY (mrbts))
        	SELECT mrbts,version
			   FROM isat_cm.mrbts WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'  GROUP BY mrbts;


        Drop table if EXISTS isat_report.susy_profile4G_macro;
        create TABLE isat_report.susy_profile4G_macro (`SITE_ID` CHAR(50) NOT NULL,
        `oss`VARCHAR(50) NULL DEFAULT NULL,
        	`mrbts` INT(11) NOT NULL,
        	`lncel` SMALLINT(5) NOT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NOT NULL DEFAULT '',
        	`mrbts_susy` INT(11) NOT NULL,
        	`BW` DOUBLE(17,0) NULL DEFAULT NULL,
        	`BAND` CHAR(50) NULL DEFAULT NULL,
        	`ANTENA` CHAR(50) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`administrativeState` SMALLINT(5) NOT NULL,
            `version` CHAR(50) NULL DEFAULT NULL,
        	PRIMARY KEY (mrbts,lncel))
        SELECT c.oss,b.siteid AS SITE_ID,a.mrbts,a.lncel,NAME,if(LEFT(NAME,1)="_",CONCAT(b.SITEID,"_IBS"),b.SITEID) AS Site_id_susy,a.mrbts AS mrbts_susy,round(c.BW,0) AS BW
		  ,c.band
		  ,if(c.dlMimoMode = 0,'SingleTX',if(c.dlMimoMode = 10,'TXDiv',if(c.dlMimoMode = 11,'4-way TXDiv',if(c.dlMimoMode = 30,'Dynamic Open Loop MIMO(2x2)',if(c.dlMimoMode = 40,'Closed Loop Mimo(2x2)',if(c.dlMimoMode = 41,'Closed Loop MIMO (4x2)',if(c.dlMimoMode = 42,'Closed Loop MIMO (8x2)',if(c.dlMimoMode = 43,'Closed Loop MIMO (4x4)',if(c.dlMimoMode = 44,'Closed Loop MIMO (8x4)',if(c.dlMimoMode = 45,'Closed Loop MIMO (16x2)','Unkown')))))))))) AS ANTENA
		  , if(LEFT(NAME,1)="_","INDOOR","MACRO") AS Remark,a.administrativeState
          ,d.version
        FROM isat_cm.lncel a
		  JOIN isat_report.list_lncel  b ON a.MRBTS = b.MRBTS AND a.LNCEL = b.LNCEL
		  JOIN isat_report.temp_lncel_fdd c ON a.MRBTS = c.mrbts AND a.LNCEL = c.LNCEL
          Left JOIN isat_report.temp_mrbts d ON a.MRBTS = d.mrbts
        WHERE a.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' AND b.siteid <> "" AND LEFT(ifnull(NAME,""),1)<>"_" GROUP BY a.mrbts,a.lncel;

        Drop table if EXISTS isat_report.susy_profile4G_ibs;
        create TABLE isat_report.susy_profile4G_ibs(`SITE_ID` CHAR(50) NOT NULL,
        	`mrbts` INT(11) NOT NULL,
        	`lncel` SMALLINT(5) NOT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NOT NULL DEFAULT '',
        	`mrbts_susy` INT(11) NOT NULL,
        	`BW` DOUBLE(17,0) NULL DEFAULT NULL,
        	`BAND` CHAR(50) NULL DEFAULT NULL,
        	`ANTENA` CHAR(50) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`administrativeState` SMALLINT(5) NOT NULL,
            `version` CHAR(50) NULL DEFAULT NULL,
			  PRIMARY KEY (mrbts,lncel))
        SELECT c.oss,b.SITEID AS SITE_ID,a.mrbts,a.lncel,NAME,if(LEFT(NAME,1)="_",d.Site_id_susy,b.SITEID) AS Site_id_susy,a.mrbts AS mrbts_susy,round(c.BW,0) AS BW,c.BAND
		  ,if(c.dlMimoMode = 0,'SingleTX',if(c.dlMimoMode = 10,'TXDiv',if(c.dlMimoMode = 11,'4-way TXDiv',if(c.dlMimoMode = 30,'Dynamic Open Loop MIMO(2x2)',if(c.dlMimoMode = 40,'Closed Loop Mimo(2x2)',if(c.dlMimoMode = 41,'Closed Loop MIMO (4x2)',if(c.dlMimoMode = 42,'Closed Loop MIMO (8x2)',if(c.dlMimoMode = 43,'Closed Loop MIMO (4x4)',if(c.dlMimoMode = 44,'Closed Loop MIMO (8x4)',if(c.dlMimoMode = 45,'Closed Loop MIMO (16x2)','Unkown')))))))))) AS ANTENA
		  , if(LEFT(NAME,1)="_","INDOOR","MACRO") AS Remark,a.administrativeState
          ,e.version
        FROM isat_cm.lncel a
		  JOIN isat_report.list_lncel b ON a.MRBTS = b.MRBTS AND a.LNCEL = b.LNCEL
		  JOIN isat_report.temp_lncel_fdd c ON a.MRBTS = c.mrbts AND a.LNCEL = c.LNCEL
		  Left JOIN isat_report.susy_temp_mrbtssiteid_ibsid d ON a.MRBTS = d.mrbts_id
          Left JOIN isat_report.temp_mrbts e ON a.MRBTS = e.mrbts
        WHERE a.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' AND b.SITEID <> "" AND LEFT(NAME,1)="_" GROUP BY a.mrbts,a.lncel;



        Drop table if EXISTS isat_report.susy_profile4G;
        create TABLE isat_report.susy_profile4G (`SITE_ID` CHAR(50) NOT NULL,
        `oss`VARCHAR(50) NULL DEFAULT NULL,
        	`mrbts` INT(11) NOT NULL,
        	`lncel` SMALLINT(5) NOT NULL,
        	`NAME` VARCHAR(50) NULL DEFAULT NULL,
        	`Site_id_susy` VARCHAR(54) NOT NULL DEFAULT '',
        	`mrbts_susy` INT(11) NOT NULL,
        	`BW` DOUBLE(17,0) NULL DEFAULT NULL,
        	`BAND` CHAR(50) NULL DEFAULT NULL,
        	`ANTENA` CHAR(50) NULL DEFAULT NULL,
        	`Remark` VARCHAR(6) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        	`administrativeState` SMALLINT(5) NOT NULL,
            `version` CHAR(50) NULL DEFAULT NULL,
        	PRIMARY KEY (mrbts,lncel))

        (SELECT oss,SITE_ID,mrbts,lncel,NAME,Site_id_susy, mrbts_susy,BW,BAND,ANTENA, Remark,administrativeState,version
        FROM isat_report.susy_profile4G_macro GROUP BY mrbts,lncel)
        UNION
        (SELECT b.oss,b.SITE_ID,b.mrbts,b.lncel,b.NAME,b.Site_id_susy, 0 AS mrbts_susy,b.BW,b.BAND,b.ANTENA, b.Remark,b.administrativeState,b.version
        FROM isat_report.susy_profile4G_macro a
        JOIN  isat_report.susy_profile4G_ibs b ON a.SITE_ID = b.SITE_ID AND a.mrbts = b.mrbts GROUP BY b.mrbts,b.lncel)
        UNION
        (SELECT  b.oss,b.SITE_ID,b.mrbts,b.lncel,b.NAME,b.Site_id_susy, b.mrbts_susy ,b.BW,b.BAND,b.ANTENA, b.Remark,b.administrativeState,b.version
        FROM isat_report.susy_profile4G_macro a
        right JOIN  isat_report.susy_profile4G_ibs b ON a.SITE_ID = b.SITE_ID AND a.mrbts = b.mrbts WHERE a.mrbts IS null GROUP BY b.mrbts,b.lncel)
        UNION
        (SELECT d.oss,b.SITEID AS SITE_ID,a.mrbts,a.lncel,a.NAME,if(LEFT(a.NAME,1)="_",e.Site_id_susy,b.SITEID) AS Site_id_susy,a.mrbts AS mrbts_susy,round(c.BW,0) AS BW,c.BAND
		  ,if(d.dlMimoMode = 0,'SingleTX',if(d.dlMimoMode = 10,'TXDiv',if(d.dlMimoMode = 11,'4-way TXDiv',if(d.dlMimoMode = 30,'Dynamic Open Loop MIMO(2x2)',if(d.dlMimoMode = 40,'Closed Loop Mimo(2x2)',if(d.dlMimoMode = 41,'Closed Loop MIMO (4x2)',if(d.dlMimoMode = 42,'Closed Loop MIMO (8x2)',if(d.dlMimoMode = 43,'Closed Loop MIMO (4x4)',if(d.dlMimoMode = 44,'Closed Loop MIMO (8x4)',if(d.dlMimoMode = 45,'Closed Loop MIMO (16x2)','Unkown')))))))))) AS ANTENA
		  , if(LEFT(a.NAME,1)="_","INDOOR","MACRO") AS Remark,a.administrativeState,f.version
        FROM isat_cm.lncel a
        JOIN isat_report.list_lncel b ON a.MRBTS = b.MRBTS AND a.LNCEL = b.LNCEL
        JOIN isat_report.temp_lncel_fdd d ON a.MRBTS = d.mrbts AND a.LNCEL = d.LNCEL
        left JOIN isat_report.susy_profile4G_macro c ON b.MRBTS = c.mrbts AND  b.LNCEL = c.lncel
        Left JOIN isat_report.susy_temp_mrbtssiteid_ibsid e ON a.MRBTS = e.mrbts_id
        Left JOIN isat_report.temp_mrbts f ON a.MRBTS = f.mrbts
		  WHERE a.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' AND b.SITEiD <> "" AND a.NAME IS null AND c.mrbts is null GROUP BY a.mrbts,a.lncel);

		Drop table if EXISTS isat_report.susy_temp_mrbtssiteid;
        Drop table if EXISTS isat_report.susy_profile4G_macro;
        Drop table if EXISTS isat_report.susy_profile4G_ibs;
        Drop table if EXISTS isat_report.temp_lncel_fdd;
        Drop table if EXISTS isat_report.susy_temp_mrbtssiteid_ibsid;
        Drop table if EXISTS isat_report.temp_mrbts

        """
    elif Request == "hwi" :
        sqlscript_query = """
            SELECT xx.oss,'""" + hwitime.strftime("%Y-%m-%d") + """' as xdate,xx.site_id,xx.siteid2G,xx.siteid3G,xx.GSMname,xx.DCSname,xx.U900name,xx.U2100name,xx.L900name,xx.L1800name,xx.L2100name,xx.bscidGSM,xx.bcfidGSM,xx.bscidDCS,xx.bcfidDCS,xx.RNCBAND900,xx.WBTSBAND900,xx.RNCBAND2100,xx.WBTSBAND2100,xx.MRBTS900,xx.MRBTS1800,xx.MRBTS2100

            ,if(GSM_COLOCATEDidentifyer = 0,"share with Macro",if(xx.bcfidGSM = n.bcfid,"share_L900",if(xx.bcfidGSM = q.bcfid,"share_L1800",if(xx.bcfidGSM = t.bcfid,"share_L900",SMOD_G900)))) AS "G900_smod"
            ,if(GSM_COLOCATEDidentifyer = 0,"share with Macro",if(xx.bcfidGSM = n.bcfId,"share_L900",if(xx.bcfidGSM = q.bcfId,L1800L900,if(xx.bcfidGSM = t.bcfId,L2100L900,RMOD_G900)))) AS "G900_rmod"
            ,if(GSM_COLOCATEDidentifyer = 0,"share with Macro",if(xx.bcfidGSM = n.bcfid,"share_L900",if(xx.bcfidGSM = q.bcfid,"share_L1800",if(xx.bcfidGSM = t.bcfid,"share_L900",TMOD_G900)))) AS "G900_tmod"

            ,if(U900_COLOCATEDidentifyer = 0,"share with Macro",if(xx.WBTSBAND900 = n.wbtsId,"share_L900",if(xx.WBTSBAND900 = q.wbtsId,"share_L1800",if(xx.WBTSBAND900 = t.wbtsId,"share_L900",SMOD_U900)))) AS "U900_smod"
            ,if(U900_COLOCATEDidentifyer = 0,"share with Macro",if(xx.WBTSBAND900 = n.wbtsId,"share_L900",if(xx.WBTSBAND900 = q.wbtsId,if(xx.bcfidGSM = q.bcfId,"sharewithGSM",L1800L900),if(xx.WBTSBAND900 = t.wbtsId,if(xx.bcfidGSM = t.bcfId,"sharewithGSM",L2100L900),RMOD_U900)))) AS "U900_rmod"
            ,if(U900_COLOCATEDidentifyer = 0,"share with Macro",if(xx.WBTSBAND900 = n.wbtsId,"share_L900",if(xx.WBTSBAND900 = q.wbtsId,"share_L1800",if(xx.WBTSBAND900 = t.wbtsId,"share_L900",TMOD_U900)))) AS "U900_tmod"


            ,if(L900_COLOCATEDidentifyer = 0,"share with Macro",L900_smod) AS L900_smod
				,if(L900_COLOCATEDidentifyer = 0,"share with Macro",L900_rmod) AS L900_rmod
				,if(L900_COLOCATEDidentifyer = 0,"share with Macro",L900_tmod) AS L900_tmod


            ,if(DCS_COLOCATEDidentifyer = 0,"share with Macro",if(xx.bcfidDCS = n.bcfid,"share_L900",if(xx.bcfidDCS = q.bcfid,"share_L1800",if(xx.bcfidDCS = t.bcfid,"share_L900",SMOD_G1800)))) AS "D1800_smod"
            ,if(DCS_COLOCATEDidentifyer = 0,"share with Macro",if(xx.bcfidDCS = q.bcfId,"share_L1800",if(xx.bcfidDCS = n.bcfId,L900L1800,if(xx.bcfidDCS = t.bcfId,L2100L1800,RMOD_G1800)))) AS "D1800_rmod"

            ,if(DCS_COLOCATEDidentifyer = 0,"share with Macro",if(xx.bcfidDCS = n.bcfid,"share_L900",if(xx.bcfidDCS = q.bcfid,"share_L1800",if(xx.bcfidDCS = t.bcfid,"share_L900",TMOD_G1800)))) AS "D1800_tmod"
			,if(L1800_COLOCATEDidentifyer = 0,"share with Macro",if(xx.MRBTS900 = xx.MRBTS1800,"Share_L900",L1800_smod)) AS L1800_smod
            ,if(L1800_COLOCATEDidentifyer = 0,"share with Macro",L1800_rmod) AS L1800_rmod
			,if(L1800_COLOCATEDidentifyer = 0,"share with Macro",if(xx.MRBTS900 = xx.MRBTS1800,"Share_L900",L1800_tmod)) AS L1800_tmod


            ,if(U2100_COLOCATEDidentifyer = 0,"share with Macro",if(xx.WBTSBAND2100 = n.wbtsId,"share_L900",if(xx.WBTSBAND2100 = q.wbtsId,"share_L1800",if(xx.WBTSBAND2100 = t.wbtsId,"share_L2100",SMOD_U2100)))) AS "U2100_smod"
            ,if(U2100_COLOCATEDidentifyer = 0,"share with Macro",if(xx.WBTSBAND2100 = t.wbtsId,"share_L2100",if(xx.WBTSBAND2100 = q.wbtsId,L1800L2100,if(xx.WBTSBAND2100 = n.wbtsId,L900L2100,RMOD_U2100)))) AS "U2100_rmod"
            ,if(U2100_COLOCATEDidentifyer = 0,"share with Macro",if(xx.WBTSBAND2100 = n.wbtsId,"share_L900",if(xx.WBTSBAND2100 = q.wbtsId,"share_L1800",if(xx.WBTSBAND2100 = t.wbtsId,"share_L2100",TMOD_U2100)))) AS "U2100_tmod"

			,if(L2100_COLOCATEDidentifyer = 0,"share with Macro",if((xx.MRBTS900 = xx.MRBTS2100),"Share_L900",if((xx.MRBTS1800 = xx.MRBTS2100),"Share_L1800",L2100_smod))) AS L2100_smod
			,if(L2100_COLOCATEDidentifyer = 0,"share with Macro",if (L1800_rmod LIKE '%AHEGC%' AND xx.MRBTS1800 IS NULL,L1800_rmod,if (L1800_rmod LIKE '%AHEGC%' AND xx.MRBTS1800 IS NOT NULL,"share_L1800",L2100_rmod))) AS L2100_rmod
			,if(L2100_COLOCATEDidentifyer = 0,"share with Macro",if((xx.MRBTS900 = xx.MRBTS2100) ,"Share_L900",if((xx.MRBTS1800 = xx.MRBTS2100),"Share_L1800",L2100_tmod))) AS L2100_tmod

            ,aa.TRX_GSM AS 'GSMTRX' ,ab.TRX_DCS AS 'DCSTRX',ac.UARFCN_900 AS 'U900Carrier',ad.UARFCN_2100 AS 'U2100Carrier'
            ,ae.BW900 'BW_L900',ae.BW1800 'BW_L1800',ae.BW2100 'BW_L2100'
				,aa.SBTS_status 'VersionGSM',ab.SBTS_status 'VersionDCS'
				,ac.SBTS_status 'VersionU900',ad.SBTS_status 'VersionU2100'
            ,xx.version_L900,xx.version_L1800,xx.version_L2100
            ,xx.antConfig_L900,xx.antConfig_L1800,xx.antConfig_L2100
            ,xx.antTypeL900,xx.antTypeL1800,xx.antTypeL2100
            ,aa.adminState_GSM,ab.adminState_DCS
            ,CONCAT("X",group_concat(ac.AdminCellState_900)) as XU900State
			,CONCAT("X",group_concat(ad.AdminCellState_2100)) as XU2100State
            ,ac.HosRemark_900 as U900HOS ,ad.HosRemark_2100 as U2100HOS
            ,ae.administrativeState900 as L900State ,ae.administrativeState1800 as L1800State ,ae.administrativeState2100 as L2100State
            ,ae.countmrbts900,ae.countmrbts1800,ae.countmrbts2100
            ,ae.RemarkHos900 as L900HOS,ae.RemarkHos1800  as L1800HOS ,ae.RemarkHos2100  as L2100HOS
            , left_position
            ,right_position
            ,L900_SN_rmod
            ,L1800_SN_rmod
            ,L2100_SN_rmod
            ,L900_SN_smod
            ,L1800_SN_smod
            ,L2100_SN_smod
            ,L900_SN_bbmod
            ,L1800_SN_bbmod
            ,L2100_SN_bbmod
            ,L900_SN_tmod
            ,L1800_SN_tmod
            ,L2100_SN_tmod


            FROM isat_report.susy_band_bw xx


            LEFT JOIN (
            SELECT a.site_id,a.MRBTS900,b.RMOD_900 AS 'L900_rmod',b.RMOD_1800 'L900L1800',b.RMOD_2100 'L900L2100',Serial_number_rmod AS 'L900_SN_rmod' FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_rmod b ON a.MRBTS900 = b.MRBTS AND a.site_id = b.SITE_ID GROUP BY a.site_id
            ) m ON xx.site_id = m.site_id



            LEFT JOIN (
            SELECT a.site_id,a.MRBTS900,b.remark AS 'L900_smod',b.wbtsId,b.bscId,b.bcfId,Serial_number_Smod AS 'L900_SN_smod',Serial_number_Bbmod AS 'L900_SN_bbmod' FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_smod b ON a.MRBTS900 = b.MRBTS AND a.site_id = b.SITE_ID GROUP BY a.site_id
            ) n ON xx.site_id = n.site_id
            LEFT JOIN (
            SELECT a.site_id,a.MRBTS900,b.remark AS 'L900_tmod',Serial_number_trmod AS 'L900_SN_tmod' FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_tmod b ON a.MRBTS900 = b.MRBTS_id AND a.site_id = b.SITE_ID GROUP BY a.site_id
            ) o ON xx.site_id = o.site_id
            #==========================================================================================
            LEFT JOIN (
            SELECT a.site_id,a.MRBTS1800,b.RMOD_1800 AS 'L1800_rmod',b.RMOD_900 AS 'L1800L900',b.RMOD_2100 AS 'L1800L2100',Serial_number_rmod AS 'L1800_SN_rmod' FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_rmod b ON a.MRBTS1800 = b.MRBTS AND a.site_id = b.SITE_ID GROUP BY a.site_id
            ) p ON xx.site_id = p.site_id




            LEFT JOIN (
            SELECT a.site_id,a.MRBTS1800,b.remark AS 'L1800_smod',b.wbtsId,b.bscId,b.bcfId,Serial_number_Smod AS 'L1800_SN_smod',Serial_number_Bbmod AS 'L1800_SN_bbmod'   FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_smod b ON a.MRBTS1800 = b.MRBTS AND a.site_id = b.SITE_ID GROUP BY a.site_id
            ) q ON xx.site_id = q.site_id
            LEFT JOIN (
            SELECT a.site_id,a.MRBTS1800,b.remark AS 'L1800_tmod',Serial_number_trmod AS 'L1800_SN_tmod' FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_tmod b ON a.MRBTS1800 = b.MRBTS_id AND a.site_id = b.SITE_ID GROUP BY a.site_id
            ) r ON xx.site_id = r.site_id
            #==========================================================================================
            LEFT JOIN (
            SELECT a.site_id,a.MRBTS2100,b.RMOD_2100 AS 'L2100_rmod',b.RMOD_900 'L2100L900' ,b.RMOD_1800 'L2100L1800',Serial_number_rmod AS 'L2100_SN_rmod' FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_rmod b ON a.MRBTS2100 = b.MRBTS AND a.site_id = b.SITE_ID GROUP BY a.site_id
            ) s ON xx.site_id = s.site_id
            LEFT JOIN (
            SELECT a.site_id,a.MRBTS2100,b.remark  AS 'L2100_smod',b.wbtsId,b.bscId,b.bcfId,Serial_number_Smod AS 'L2100_SN_smod',Serial_number_Bbmod AS 'L2100_SN_bbmod' FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_smod b ON a.MRBTS2100 = b.MRBTS AND a.site_id = b.SITE_ID GROUP BY a.site_id
            ) t ON xx.site_id = t.site_id
            LEFT JOIN (
            SELECT a.site_id,a.MRBTS2100,b.remark AS 'L2100_tmod',Serial_number_trmod AS 'L2100_SN_tmod' FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_tmod b ON a.MRBTS2100 = b.MRBTS_id AND a.site_id = b.SITE_ID GROUP BY a.site_id
            ) u ON xx.site_id = u.site_id
            #==========================================================================================
            LEFT JOIN (
            SELECT a.site_id
            ,b.RMOD_G900,b.RMOD_G1800,b.RMOD_U900,b.RMOD_U2100,b.RMOD_L900,b.RMOD_L1800,b.RMOD_L2100

            ,b.SMOD_G900,b.SMOD_G1800,b.SMOD_U900,b.SMOD_U2100,b.SMOD_L900,b.SMOD_L1800,b.SMOD_L2100

            ,b.TMOD_G900,b.TMOD_G1800,b.TMOD_U900,b.TMOD_U2100,b.TMOD_L900,b.TMOD_L1800,b.TMOD_L2100
             FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_nonsran_submodule b ON  a.site_id = b.SITE_ID GROUP BY a.site_id
            ) v ON xx.site_id = v.site_id
            #==========================================================================================

            LEFT JOIN isat_report.susy_hwi_2gtrx aa ON xx.site_id = aa.SITE_ID AND xx.bscidGSM = aa.bsc AND xx.bcfidGSM = aa.bcf

            LEFT JOIN isat_report.susy_hwi_2gtrx ab ON xx.site_id = ab.SITE_ID AND xx.bscidDCS = ab.bsc AND xx.bcfidDCS = ab.bcf

            LEFT JOIN isat_report.susy_hwi_3guarfcn ac ON xx.site_id = ac.SITE_ID AND xx.RNCBAND900 = ac.RNC AND xx.WBTSBAND900 = ac.WBTS

            LEFT JOIN isat_report.susy_hwi_3guarfcn ad ON xx.site_id = ad.SITE_ID AND xx.RNCBAND2100 = ad.RNC AND xx.WBTSBAND2100 = ad.WBTS

            LEFT JOIN isat_report.susy_bw4g ae ON xx.site_id = ae.SITE_ID

            LEFT JOIN (select SIte_ID,concat(GROUP_CONCAT(DISTINCT concat(mrbts,"|",LEFT_loc) SEPARATOR '|'),"|",GROUP_CONCAT(DISTINCT concat(mrbts,"|",BBLEFT_loc) SEPARATOR '|')) AS left_position
            ,concat(GROUP_CONCAT(DISTINCT concat(mrbts,"|",RIGHT_loc) SEPARATOR '|'),"|",GROUP_CONCAT(DISTINCT concat(mrbts,"|",BBRIGHT_loc) SEPARATOR '|')) AS right_position
				from isat_report.susy_hwi_smod_loc GROUP BY SIte_ID) af  ON xx.site_id = af.SITE_ID
            WHERE xx.site_id <> ""
            GROUP BY xx.site_id

            """
    elif Request == "hwi_update_1":
        sqlscript_query = """
        TRUNCATE isat_report.susysiteidlist;
        REPLACE INTO isat_report.susysiteidlist

        (SELECT a.Site_id_susy AS SITE_ID,a.oss
        FROM isat_report.susy_profile2G a
        where IFNULL(a.Site_id_susy,'')<>''
        GROUP BY a.Site_id_susy)

        UNION

        (SELECT b.Site_id_susy AS SITE_ID,b.oss
        FROM isat_report.susy_profile3G b
        where ifnull(b.Site_id_susy,'')<>''
        GROUP BY b.Site_id_susy)

        UNION

        (SELECT c.Site_id_susy AS SITE_ID,c.oss
        FROM isat_report.susy_profile4G c
        where ifnull(c.Site_id_susy,'')<>''
        GROUP BY c.Site_id_susy)
        """
    elif Request == "hwi_update_2":
        sqlscript_query = """
        Drop table if EXISTS isat_report.susy_rmod_r;
        create TABLE isat_report.susy_rmod_r (
                `oss` VARCHAR(100) NOT NULL,
        	`xdate` DATE NOT NULL,
        	`distName` VARCHAR(100) NOT NULL,
        	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
        	`EQM` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`APEQM` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`RMOD` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`aldManagementProtocol` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`blocking` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`configDN` VARCHAR(50) NULL DEFAULT NULL,
        	`hwVersion` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
        	`operationalState` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`productCode` VARCHAR(50) NULL DEFAULT NULL,
        	`productName` VARCHAR(50) NULL DEFAULT NULL,
        	`radioMasterDN` VARCHAR(50) NULL DEFAULT NULL,
        	`serialNumber` VARCHAR(50) NULL DEFAULT NULL,
        	`class` VARCHAR(100) NULL DEFAULT NULL,
        	`defaults` VARCHAR(50) NULL DEFAULT NULL,
        	`filename` VARCHAR(255) NULL DEFAULT NULL,
        	`antennaPathDelayMeasurementCapable` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`radioModuleHwReleaseCode` VARCHAR(50) NULL DEFAULT NULL,
        	`rfmTransmitModeStatus` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`availabilityStatus` VARCHAR(50) NULL DEFAULT NULL,
        	`distidentifier` VARCHAR(100) NULL DEFAULT NULL,
        	`siteId` VARCHAR(100) NULL DEFAULT NULL,
        	`siteCId` VARCHAR(100) NULL DEFAULT NULL,
        	`administrativeState` VARCHAR(100) NULL DEFAULT NULL,
        	`chassisProductCode` VARCHAR(100) NULL DEFAULT NULL,
        	`chassisSerialNumber` VARCHAR(100) NULL DEFAULT NULL,
        	`nrOfTXElements` VARCHAR(100) NULL DEFAULT NULL,
        	`proceduralStatus` VARCHAR(100) NULL DEFAULT NULL,
        	PRIMARY KEY (configDN,distName))

		  	SELECT oss,xdate,distName,MRBTS
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"EQM")+4,INSTR(a.configDN,"APEQM")-INSTR(a.configDN,"EQM")-5),EQM_R) AS EQM
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"APEQM")+6,INSTR(a.configDN,"RMOD")-INSTR(a.configDN,"APEQM")-7),APEQM_R) AS APEQM
        	, ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"RMOD")+5,1),rmod_r) AS rmod
        	,aldManagementProtocol,blocking,configDN,hwVersion,operationalState,productCode,productName,radioMasterDN,serialNumber
            ,class,defaults,filename,antennaPathDelayMeasurementCapable,radioModuleHwReleaseCode,rfmTransmitModeStatus
            ,availabilityStatus,distidentifier,siteId,siteCId,administrativeState,chassisProductCode,chassisSerialNumber
            ,nrOfTXElements,proceduralStatus
	FROM isat_cm.rmod_r a
	WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'  GROUP BY configDN,distName;

    Drop table if EXISTS isat_report.susy_hwi_rmod;
    CREATE TABLE isat_report.susy_hwi_rmod (
    	`SITE_ID` VARCHAR(54) NOT NULL,
    	`mrbts` INT(11) NOT NULL,
    	`FRGU` BIGINT(21) NOT NULL DEFAULT '0',
    	`FXDB` BIGINT(21) NOT NULL DEFAULT '0',
        `ARGA` BIGINT(21) NOT NULL DEFAULT '0',
    	`FXDA` BIGINT(21) NOT NULL DEFAULT '0',
    	`FXED` BIGINT(21) NOT NULL DEFAULT '0',
    	`FXEB` BIGINT(21) NOT NULL DEFAULT '0',
    	`FXEA` BIGINT(21) NOT NULL DEFAULT '0',
    	`FRGP` BIGINT(21) NOT NULL DEFAULT '0',
    	`FR2EA` BIGINT(21) NOT NULL DEFAULT '0',
    	`FR2GA` BIGINT(21) NOT NULL DEFAULT '0',
    	`FR2EC` BIGINT(21) NOT NULL DEFAULT '0',
    	`FRGT` BIGINT(21) NOT NULL DEFAULT '0',
    	`FRGX` BIGINT(21) NOT NULL DEFAULT '0',
    	`FXDD` BIGINT(21) NOT NULL DEFAULT '0',
    	`FXCA` BIGINT(21) NOT NULL DEFAULT '0',
    	`FXDJ` BIGINT(21) NOT NULL DEFAULT '0',
    	`FRGC` BIGINT(21) NOT NULL DEFAULT '0',
    	`FRGD` BIGINT(21) NOT NULL DEFAULT '0',
    	`FRGF` BIGINT(21) NOT NULL DEFAULT '0',
        `AHEGC` BIGINT(21) NOT NULL DEFAULT '0',
        `AREA` BIGINT(21) NOT NULL DEFAULT '0',
        `AHDA` BIGINT(21) NOT NULL DEFAULT '0',
        `FHDB` BIGINT(21) NOT NULL DEFAULT '0',

    	`RMOD_900` VARCHAR(135) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
    	`RMOD_1800` VARCHAR(81) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
    	`RMOD_2100` VARCHAR(189) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
        `Serial_number_rmod` VARCHAR(189) NOT NULL DEFAULT '0',

        PRIMARY KEY (SITE_ID,mrbts))
        SELECT a.Site_id_susy AS SITE_ID, a.mrbts
        ,ifnull(c.FRGU,0) 'FRGU'
        ,ifnull(b.FXDB,0) 'FXDB'
        ,ifnull(ARGA,0) 'ARGA'
        ,ifnull(FXDA,0) 'FXDA'
        ,ifnull(FXED,0) 'FXED'
        ,ifnull(FXEB,0) 'FXEB'
        ,ifnull(FXEA,0) 'FXEA'
        ,ifnull(FRGP,0) 'FRGP'
        ,ifnull(FR2EA,0) 'FR2EA'
        ,ifnull(FR2GA,0) 'FR2GA'
        ,ifnull(FR2EC,0) 'FR2EC'
        ,ifnull(FRGT,0) 'FRGT'
        ,ifnull(FRGX,0) 'FRGX'
        ,ifnull(FXDD,0) 'FXDD'
        ,ifnull(FXCA,0) 'FXCA'
        ,ifnull(FXDJ,0) 'FXDJ'
		,ifnull(FRGC,0) 'FRGC'
		,ifnull(FRGD,0) 'FRGD'
		,ifnull(FRGF,0) 'FRGF'
        ,ifnull(AHEGC,0) 'AHEGC'
        ,ifnull(AREA,0) 'AREA'
        ,ifnull(AREA,0) 'AHDA'
        ,ifnull(FHDB,0) 'FHDB'

        ,concat(ifnull(concat(FXDA,"_FXDA "),""),ifnull(concat(FXDB,"_FXDB "),""),ifnull(concat(FXCA,"_FXCA "),""),ifnull(concat(FXDJ,"_FXDJ "),""),ifnull(concat(FXDD,"_FXDD "),""),ifnull(concat(AHDA,"_AHDA "),""),ifnull(concat(FHDB,"_FHDB "),"")) AS 'RMOD_900'
        ,concat(ifnull(concat(FXEA,"_FXEA "),""),ifnull(concat(FXEB,"_FXEB "),""),ifnull(concat(FXED,"_FXED "),""),ifnull(concat(AHEGC,"_AHEGC "),""),ifnull(concat(AREA,"_AREA "),""),ifnull(concat(FR2EA,"_FR2EA "),""),ifnull(concat(FR2EC,"_FR2EC "),"")) AS 'RMOD_1800'
        ,concat(ifnull(concat(ARGA,"_ARGA "),""),ifnull(concat(FRGU,"_FRGU "),""),ifnull(concat(FRGT,"_FRGT "),""),ifnull(concat(FRGX,"_FRGX "),""),ifnull(concat(FRGP,"_FRGP "),""),ifnull(concat(FRGC,"_FRGC "),""),ifnull(concat(FRGD,"_FRGD "),""),ifnull(concat(FRGF,"_FRGF "),""),ifnull(concat(FR2GA,"_FR2GA "),"")) AS 'RMOD_2100'
        ,concat(ifnull(concat(SN_FXDB ,"_FXDB "),""),ifnull(concat(SN_FRGU ,"_FRGU "),""),ifnull(concat(SN_FXDA ,"_FXDA "),""),ifnull(concat(SN_FXED ,'_FXED '),"")
		 ,ifnull(concat(SN_FXEB ,'_FXEB '),""),ifnull(concat(SN_FXEA ,'_FXEA '),""),ifnull(concat(SN_FRGP ,'_FRGP '),""),ifnull(concat(SN_FR2EA ,'_FR2EA '),"")
		 ,ifnull(concat(SN_FR2GA ,'_FR2GA '),""),ifnull(concat(SN_FR2EC ,'_FR2EC '),""),ifnull(concat(SN_FRGT ,'_FRGT '),""),ifnull(concat(SN_FRGX ,'_FRGX '),"")
		 ,ifnull(concat(SN_FXDD ,'_FXDD '),""),ifnull(concat(SN_FXCA ,'_FXCA '),""),ifnull(concat(SN_FXDJ ,'_FXDJ '),""),ifnull(concat(SN_FRGC ,'_FRGC '),"")
		 ,ifnull(concat(SN_FRGD ,'_FRGD '),""),ifnull(concat(SN_FRGF ,'_FRGF '),""),ifnull(concat(SN_AHEGC ,'_AHEGC '),""),ifnull(concat(SN_AREA ,'_AREA '),"")
		 ,ifnull(concat(SN_AHDA ,'_AHDA '),""),ifnull(concat(SN_FHDB ,'_FHDB '),""),ifnull(concat(SN_ARGA ,'_ARGA '),"")) AS Serial_number_rmod
        FROM
        isat_report.susy_profile4g a
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FXDB',group_concat(serialNumber separator "-") AS SN_FXDB
        FROM isat_report.susy_rmod_r WHERE productName = 'FXDB' GROUP BY mrbts,productName) b
        ON a.mrbts = b.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FRGU',group_concat(serialNumber separator "-") AS SN_FRGU
        FROM isat_report.susy_rmod_r WHERE productName = 'FRGU' GROUP BY mrbts,productName ) c
        ON a.mrbts = c.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FXDA',group_concat(serialNumber separator "-") AS SN_FXDA
        FROM isat_report.susy_rmod_r WHERE productName = 'FXDA' GROUP BY mrbts,productName ) d
        ON a.mrbts = d.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FXED',group_concat(serialNumber separator "-") AS SN_FXED
        FROM isat_report.susy_rmod_r WHERE productName = 'FXED' GROUP BY mrbts,productName ) e
        ON a.mrbts = e.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FXEB',group_concat(serialNumber separator "-") AS SN_FXEB
        FROM isat_report.susy_rmod_r WHERE productName = 'FXEB' GROUP BY mrbts,productName ) f
        ON a.mrbts = f.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FXEA',group_concat(serialNumber separator "-") AS SN_FXEA
        FROM isat_report.susy_rmod_r WHERE productName = 'FXEA' GROUP BY mrbts,productName ) g
        ON a.mrbts = g.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FRGP',group_concat(serialNumber separator "-") AS SN_FRGP
        FROM isat_report.susy_rmod_r WHERE productName = 'FRGP' GROUP BY mrbts,productName ) h
        ON a.mrbts = h.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FR2EA',group_concat(serialNumber separator "-") AS SN_FR2EA
        FROM isat_report.susy_rmod_r WHERE productName = 'FR2EA' GROUP BY mrbts,productName ) i
        ON a.mrbts = i.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FR2GA',group_concat(serialNumber separator "-") AS SN_FR2GA
        FROM isat_report.susy_rmod_r WHERE productName = 'FR2GA' GROUP BY mrbts,productName ) j
        ON a.mrbts = j.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FR2EC',group_concat(serialNumber separator "-") AS SN_FR2EC
        FROM isat_report.susy_rmod_r WHERE productName = 'FR2EC' GROUP BY mrbts,productName ) k
        ON a.mrbts = k.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FRGT',group_concat(serialNumber separator "-") AS SN_FRGT
        FROM isat_report.susy_rmod_r WHERE productName = 'FRGT' GROUP BY mrbts,productName ) l
        ON a.mrbts = l.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FRGX',group_concat(serialNumber separator "-") AS SN_FRGX
        FROM isat_report.susy_rmod_r WHERE productName = 'FRGX' GROUP BY mrbts,productName ) m
        ON a.mrbts = m.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FXDD',group_concat(serialNumber separator "-") AS SN_FXDD
        FROM isat_report.susy_rmod_r WHERE productName = 'FXDD' GROUP BY mrbts,productName ) o
        ON a.mrbts = o.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FXCA',group_concat(serialNumber separator "-") AS SN_FXCA
        FROM isat_report.susy_rmod_r WHERE productName = 'FXCA' GROUP BY mrbts,productName ) p
        ON a.mrbts = m.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FXDJ',group_concat(serialNumber separator "-") AS SN_FXDJ
        FROM isat_report.susy_rmod_r WHERE productName = 'FXDJ' GROUP BY mrbts,productName ) q
        ON a.mrbts = m.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FRGC',group_concat(serialNumber separator "-") AS SN_FRGC
        FROM isat_report.susy_rmod_r WHERE productName = 'FRGC' GROUP BY mrbts,productName ) r
        ON a.mrbts = m.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FRGD',group_concat(serialNumber separator "-") AS SN_FRGD
        FROM isat_report.susy_rmod_r WHERE productName = 'FRGD' GROUP BY mrbts,productName ) s
        ON a.mrbts = m.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FRGF',group_concat(serialNumber separator "-") AS SN_FRGF
        FROM isat_report.susy_rmod_r WHERE productName = 'FRGF' GROUP BY mrbts,productName ) t
        ON a.mrbts = m.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'AHEGC',group_concat(serialNumber separator "-") AS SN_AHEGC
        FROM isat_report.susy_rmod_r WHERE productName = 'AHEGC' GROUP BY mrbts,productName ) u
        ON a.mrbts = u.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'AREA',group_concat(serialNumber separator "-") AS SN_AREA
        FROM isat_report.susy_rmod_r WHERE productName = 'AREA' GROUP BY mrbts,productName ) v
        ON a.mrbts = v.mrbts

        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'AHDA',group_concat(serialNumber separator "-") AS SN_AHDA
        FROM isat_report.susy_rmod_r WHERE productName = 'AHDA' GROUP BY mrbts,productName ) w
        ON a.mrbts = w.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FHDB',group_concat(serialNumber separator "-") AS SN_FHDB
        FROM isat_report.susy_rmod_r WHERE productName = 'FHDB' GROUP BY mrbts,productName ) x
        ON a.mrbts = x.mrbts
        left JOIN (
        SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'ARGA',group_concat(serialNumber separator "-") AS SN_ARGA
        FROM isat_report.susy_rmod_r WHERE productName = 'ARGA' GROUP BY mrbts,productName ) y
        ON a.mrbts = y.mrbts



        WHERE ifnull(a.Site_id_susy ,'')<>''
        GROUP BY a.Site_id_susy,a.mrbts;
        Drop table if EXISTS isat_report.susy_rmod_r;
        """
    elif Request == "hwi_update_3":

        sqlscript_query = """
        Drop table if EXISTS isat_report.susy_smod_r;
        create TABLE isat_report.susy_smod_r (
        	`oss` VARCHAR(100) NOT NULL,
        	`xdate` DATE NOT NULL,
        	`distName` VARCHAR(100) NOT NULL,
        	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
        	`EQM` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`APEQM` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`CABINET` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`SMOD` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`id` INT(10) UNSIGNED NULL DEFAULT NULL,
        	`configDN` VARCHAR(50) NULL DEFAULT NULL,
        	`function` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`horizontalPosition` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`operationalState` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`productCode` VARCHAR(50) NULL DEFAULT NULL,
        	`productName` VARCHAR(50) NULL DEFAULT NULL,
        	`serialNumber` VARCHAR(50) NULL DEFAULT NULL,
        	`verticalPosition` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`class` VARCHAR(100) NULL DEFAULT NULL,
        	`defaults` VARCHAR(50) NULL DEFAULT NULL,
        	`filename` VARCHAR(255) NULL DEFAULT NULL,
        	`eutraSupport` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`utranSupport` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`geranSupport` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`activeRole` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`availabilityStatus` VARCHAR(50) NULL DEFAULT NULL,
        	`distidentifier` VARCHAR(100) NULL DEFAULT NULL,
        	`siteId` VARCHAR(100) NULL DEFAULT NULL,
        	`siteCId` VARCHAR(100) NULL DEFAULT NULL,
        	`proceduralStatus` VARCHAR(100) NULL DEFAULT NULL,
            PRIMARY KEY (configDN,distName,MRBTS))

        	SELECT oss,xdate,distName,MRBTS
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"EQM")+4,INSTR(a.configDN,"APEQM")-INSTR(a.configDN,"EQM")-5),EQM_R) AS EQM
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"APEQM")+6,INSTR(a.configDN,"CABINET")-INSTR(a.configDN,"APEQM")-7),APEQM_R) AS APEQM
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"CABINET")+8,INSTR(a.configDN,"SMOD")-INSTR(a.configDN,"CABINET")-9),CABINET_R) AS CABINET
        	, ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"SMOD")+5,1),SMOD_R) AS SMOD
        	,id,configDN,FUNCTION,horizontalPosition,operationalState,productCode,productName,serialNumber,verticalPosition,class,defaults,filename
        	,eutraSupport,utranSupport,geranSupport,activeRole,availabilityStatus,distidentifier,siteId,siteCId
			  ,proceduralStatus
        	FROM isat_cm.smod_r a
        	WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' GROUP BY configDN,distName;

        Drop table if EXISTS isat_report.susy_bbmod_r;
        create TABLE isat_report.susy_bbmod_r (
        	`oss` VARCHAR(100) NOT NULL,
        	`xdate` DATE NOT NULL,
        	`distName` VARCHAR(100) NOT NULL,
        	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
        	`EQM` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`APEQM` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`CABINET` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`BBMOD` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`configDN` VARCHAR(50) NULL DEFAULT NULL,
        	`eutraSupport` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`function` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`geranSupport` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`horizontalPosition` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`operationalState` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`productCode` VARCHAR(50) NULL DEFAULT NULL,
        	`productName` VARCHAR(50) NULL DEFAULT NULL,
        	`serialNumber` VARCHAR(50) NULL DEFAULT NULL,
        	`utranSupport` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`verticalPosition` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`class` VARCHAR(100) NULL DEFAULT NULL,
        	`defaults` VARCHAR(50) NULL DEFAULT NULL,
        	`filename` VARCHAR(255) NULL DEFAULT NULL,
        	`availabilityStatus` VARCHAR(50) NULL DEFAULT NULL,
        	`distidentifier` VARCHAR(100) NULL DEFAULT NULL,
        	`administrativeState` VARCHAR(100) NULL DEFAULT NULL,
        	`proceduralStatus` VARCHAR(100) NULL DEFAULT NULL,
                	PRIMARY KEY (configDN,distName,MRBTS))

        		  	SELECT oss,xdate,distName,MRBTS
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"EQM")+4,INSTR(a.configDN,"APEQM")-INSTR(a.configDN,"EQM")-5),EQM_R) AS EQM
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"APEQM")+6,INSTR(a.configDN,"CABINET")-INSTR(a.configDN,"APEQM")-7),APEQM_R) AS APEQM
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"CABINET")+8,INSTR(a.configDN,"BBMOD")-INSTR(a.configDN,"CABINET")-9),CABINET_R) AS CABINET
        	, ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"BBMOD")+6,1),BBMOD_R) AS BBMOD
        ,configDN,eutraSupport,FUNCTION,geranSupport,horizontalPosition,operationalState,productCode,productName,serialNumber,utranSupport,verticalPosition
        ,class,defaults,filename,availabilityStatus,distidentifier,administrativeState,proceduralStatus
        	FROM isat_cm.bbmod_r a
        	WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """'  GROUP BY configDN,distName;


        Drop table if EXISTS isat_report.susy_relation3g;
        create TABLE isat_report.susy_relation3g (
         `xdate` DATE NOT NULL,
        	`mrbts` INT(11) NOT NULL,
        	`wbtsid` INT(11) NOT NULL,
        	PRIMARY KEY (mrbts,wbtsid))
        (select xdate,mrbts,wbtsid from isat_cm.wnbts  WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' AND wbtsid IS NOT null AND mrbts IS NOT null
		  GROUP BY mrbts)
        UNION
        (select xdate, SBTSId AS mrbts,b.WBTS AS wbtsid from isat_cm.wbts  b
		  WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' AND WBTS IS NOT null AND SBTSId IS NOT null GROUP BY SBTSId);

		Drop table if EXISTS isat_report.susy4g_temp;
        create TABLE isat_report.susy4g_temp(
			`MRBTS` INT(11) NOT NULL,
			`Band` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			PRIMARY KEY (MRBTS))
		select mrbts,GROUP_CONCAT(DISTINCT band ORDER BY band ASC SEPARATOR ',') as Band  from isat_report.susy_profile4g GROUP BY mrbts;
Drop table if EXISTS isat_report.susy3g_temp;
        create TABLE isat_report.susy3g_temp(
			`sbtsid` INT(11) NOT NULL,
			`Band` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			PRIMARY KEY (sbtsid))
		select sbtsid,GROUP_CONCAT(DISTINCT band ORDER BY band ASC SEPARATOR ',') as Band  from isat_report.susy_profile3g GROUP BY sbtsid;
Drop table if EXISTS isat_report.susy2g_temp;
        create TABLE isat_report.susy2g_temp(
			`sbtsid` INT(11) NOT NULL,
			`Band` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			PRIMARY KEY (sbtsid))
		select sbtsid,GROUP_CONCAT(DISTINCT band ORDER BY band ASC SEPARATOR ',') as Band from isat_report.susy_profile2g GROUP BY sbtsid;

Drop table if EXISTS isat_report.susy2g3g4gband_ref;
        create TABLE isat_report.susy2g3g4gband_ref(
			`mrbts` INT(11) NOT NULL,
			`Band4g` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			`Band3g` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			`Band2g` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			PRIMARY KEY (mrbts))
SELECT mrbts
,if(a.band = "1800","18",if(a.band="900","9",if(a.band="2100","21",if(a.band="1800,900","9&18",if(a.band="1800,2100,900","9&18&21",if(a.band="1800,2100","18&21",a.band)))))) AS Band4g
,if(b.band = "2100","21",if(b.band="900","9",if(b.band="2100,900","9&21",b.band))) AS Band3g
,if(c.band = "1800","18",if(c.band="900","9",if(c.band="1800,900","9&18",c.band))) AS Band2g
		FROM isat_report.susy4g_temp  a
		LEFT JOIN isat_report.susy3g_temp b ON a.mrbts = b.sbtsid
		LEFT JOIN isat_report.susy2g_temp c ON a.mrbts = c.sbtsid ;


		Drop table if EXISTS isat_report.susy2g_temp;
		Drop table if EXISTS isat_report.susy3g_temp;
		Drop table if EXISTS isat_report.susy4g_temp;

DROP TABLE IF EXISTS isat_report.susy_smod_Right;
CREATE TABLE isat_report.susy_smod_Right(
 	`xdate` DATE NOT NULL,
			`MRBTS` INT(11) NOT NULL,
			`distName` VARCHAR(100) NOT NULL,
			`productName` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			`horizontalPosition` INT(11) NOT NULL,
			`verticalPosition` INT(11) NOT NULL,
			`tech` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci', PRIMARY KEY (MRBTS,distName))
SELECT xdate,a.mrbts
			,
REPLACE(
REPLACE(productName, 'Flexi System Module Outdoor FSMF','FSMF'),'ASIA AirScale Common','ASIA') AS productName
			,horizontalPosition,verticalPosition,distName
			, CONCAT(IF(a.eutraSupport = 1, CONCAT("L", IFNULL(b.Band4g,""),","),"")
		, IF(a.utranSupport = 1, CONCAT("W", IFNULL(b.Band3g,""),","),"")
, IF(a.geranSupport = 1, CONCAT("G", IFNULL(b.Band2g,"")),"")) AS Tech
FROM isat_report.susy_smod_r a
JOIN isat_report.susy2g3g4gband_ref b ON a.mrbts = b. mrbts
WHERE horizontalPosition = 2 ;
DROP TABLE IF EXISTS isat_report.susy_smod_left;
CREATE TABLE isat_report.susy_smod_left(
 	`xdate` DATE NOT NULL,
			`MRBTS` INT(11) NOT NULL,
			`distName` VARCHAR(100) NOT NULL,
			`productName` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			`horizontalPosition` INT(11) NOT NULL,
			`verticalPosition` INT(11) NOT NULL,
			`tech` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci', PRIMARY KEY (MRBTS,distName))
SELECT xdate,a.mrbts
			,
REPLACE(
REPLACE(productName, 'Flexi System Module Outdoor FSMF','FSMF'),'ASIA AirScale Common','ASIA') AS productName
			,horizontalPosition,verticalPosition,distName
, CONCAT(IF(a.eutraSupport = 1, CONCAT("L", IFNULL(b.Band4g,""),","),"")
		, IF(a.utranSupport = 1, CONCAT("W", IFNULL(b.Band3g,""),","),"")
, IF(a.geranSupport = 1, CONCAT("G", IFNULL(b.Band2g,"")),"")) AS Tech
FROM isat_report.susy_smod_r a
JOIN isat_report.susy2g3g4gband_ref b ON a.mrbts = b. mrbts
WHERE horizontalPosition = 1 ;
DROP TABLE IF EXISTS isat_report.susy_bbmod_Right;
CREATE TABLE isat_report.susy_bbmod_Right(
 	`xdate` DATE NOT NULL,
			`MRBTS` INT(11) NOT NULL,
			`distName` VARCHAR(100) NOT NULL,
			`productName` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			`horizontalPosition` INT(11) NOT NULL,
			`verticalPosition` INT(11) NOT NULL,
			`tech` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci', PRIMARY KEY (MRBTS,distName))
SELECT xdate,a.mrbts
			,
REPLACE(
REPLACE(
REPLACE(productName, 'Flexi Baseband Sub-Module FBBC','FBBC'),'BB Extension Outdoor Sub-Module FBBA','FBBA'),'ABIA AirScale Capacity','ABIA') AS productName
			,horizontalPosition,verticalPosition,distName
			, CONCAT(IF(a.eutraSupport = 1, CONCAT("L", IFNULL(b.Band4g,""),","),"")
		, IF(a.utranSupport = 1, CONCAT("W", IFNULL(b.Band3g,""),","),"")
, IF(a.geranSupport = 1, CONCAT("G", IFNULL(b.Band2g,"")),"")) AS Tech
FROM isat_report.susy_bbmod_r a
JOIN isat_report.susy2g3g4gband_ref b ON a.mrbts = b. mrbts
WHERE horizontalPosition = 2 ;
DROP TABLE IF EXISTS isat_report.susy_bbmod_left;
CREATE TABLE isat_report.susy_bbmod_left(
 	`xdate` DATE NOT NULL,
			`MRBTS` INT(11) NOT NULL,
			`distName` VARCHAR(100) NOT NULL,
			`productName` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			`horizontalPosition` INT(11) NOT NULL,
			`verticalPosition` INT(11) NOT NULL,
			`tech` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci', PRIMARY KEY (MRBTS,distName))
SELECT xdate,a.mrbts
			,
REPLACE(
REPLACE(
REPLACE(productName, 'Flexi Baseband Sub-Module FBBC','FBBC'),'BB Extension Outdoor Sub-Module FBBA','FBBA'),'ABIA AirScale Capacity','ABIA') AS productName
			,horizontalPosition,verticalPosition,distName
, CONCAT(IF(a.eutraSupport = 1, CONCAT("L", IFNULL(b.Band4g,""),","),"")
		, IF(a.utranSupport = 1, CONCAT("W", IFNULL(b.Band3g,""),","),"")
, IF(a.geranSupport = 1, CONCAT("G", IFNULL(b.Band2g,"")),"")) AS Tech
FROM isat_report.susy_bbmod_r a
JOIN isat_report.susy2g3g4gband_ref b ON a.mrbts = b. mrbts
WHERE horizontalPosition = 1 ;

        Drop table if EXISTS isat_report.susy2g3g4gband_ref;

Drop table if EXISTS isat_report.susy_hwi_smod_loc;
        create TABLE isat_report.susy_hwi_smod_loc(
        	`SITE_ID` VARCHAR(100) NOT NULL,
			`MRBTS` INT(11) NOT NULL,
			`LEFT_loc` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			`RIGHT_loc` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			`BBLEFT_loc` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			`BBRIGHT_loc` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
			PRIMARY KEY (SITE_ID,MRBTS))
SELECT a.Site_id_susy as SITE_ID, a.MRBTS
,GROUP_CONCAT(DISTINCT CONCAT(b.verticalPosition,".",b.productName,"(",b.Tech,")") ORDER BY b.verticalPosition ASC SEPARATOR '|') AS LEFT_loc
,GROUP_CONCAT(DISTINCT concat(c.verticalPosition,".",c.productName,"(",c.Tech,")") ORDER BY c.verticalPosition ASC SEPARATOR '|') AS RIGHT_loc
,GROUP_CONCAT(DISTINCT concat(d.verticalPosition,".",d.productName,"(",d.Tech,")") ORDER BY d.verticalPosition ASC SEPARATOR '|') AS BBLEFT_loc
,GROUP_CONCAT(DISTINCT concat(e.verticalPosition,".",e.productName,"(",e.Tech,")") ORDER BY e.verticalPosition ASC SEPARATOR '|') AS BBRIGHT_loc
FROM isat_report.susy_profile4g a
        left JOIN  isat_report.susy_smod_left b ON a.mrbts = b.mrbts
        left JOIN  isat_report.susy_smod_Right c ON a.mrbts = c.mrbts
        left JOIN isat_report.susy_bbmod_left d ON a.mrbts = d.mrbts
        left JOIN isat_report.susy_bbmod_Right e ON a.mrbts = e.mrbts
        WHERE IFNULL(a.Site_id_susy,'')<>''
        GROUP BY a.Site_id_susy,a.mrbts;

        Drop table if EXISTS isat_report.susy_smod_left;
        Drop table if EXISTS isat_report.susy_smod_Right;
        Drop table if EXISTS isat_report.susy_bbmod_left;
        Drop table if EXISTS isat_report.susy_bbmod_Right;


Drop table if EXISTS isat_report.susy_temp2g4g;
        create TABLE isat_report.susy_temp2g4g(
			`xdate` DATE NOT NULL,`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL
			,`bscId` MEDIUMINT(8) UNSIGNED NULL DEFAULT NULL
			,`bcfId` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS,bscId,bcfId))
select xdate,mrbts,bscid,bcfId from isat_cm.gnbcf  WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' GROUP BY mrbts;


		Drop table if EXISTS isat_report.susy_tempfsmf;
        create TABLE isat_report.susy_tempfsmf(
			`xdate` DATE NOT NULL
			,`mrbts` MEDIUMINT(9) NULL DEFAULT NULL
			,`productName` VARCHAR(50) NULL DEFAULT NULL
			,`FSMF` MEDIUMINT(9) NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS))
		SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FSMF',group_concat(serialNumber separator "-") AS SN_FSMF
        FROM isat_report.susy_smod_r WHERE  productName = 'Flexi System Module Outdoor FSMF' GROUP BY mrbts,productName;


			Drop table if EXISTS isat_report.susy_tempFW2GEA;
        create TABLE isat_report.susy_tempFW2GEA(
			`xdate` DATE NOT NULL
			,`mrbts` MEDIUMINT(9) NULL DEFAULT NULL
			,`productName` VARCHAR(50) NULL DEFAULT NULL
			,`FW2GEA` MEDIUMINT(9) NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS))
		SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FW2GEA',group_concat(serialNumber separator "-") AS SN_FW2GEA
        FROM isat_report.susy_smod_r WHERE  productName = 'FW2GEA' GROUP BY mrbts,productName;

        Drop table if EXISTS isat_report.susy_tempFW2EA;
        create TABLE isat_report.susy_tempFW2EA(
			`xdate` DATE NOT NULL
			,`mrbts` MEDIUMINT(9) NULL DEFAULT NULL
			,`productName` VARCHAR(50) NULL DEFAULT NULL
			,`FW2EA` MEDIUMINT(9) NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS))
		SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FW2EA',group_concat(serialNumber separator "-") AS SN_FW2EA
        FROM isat_report.susy_smod_r WHERE  productName = 'FW2EA' GROUP BY mrbts,productName;

			Drop table if EXISTS isat_report.susy_tempFBBC;
        create TABLE isat_report.susy_tempFBBC(
			`xdate` DATE NOT NULL
			,`mrbts` MEDIUMINT(9) NULL DEFAULT NULL
			,`productName` VARCHAR(50) NULL DEFAULT NULL
			,`FBBC` MEDIUMINT(9) NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS))
			SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FBBC',group_concat(serialNumber separator "-") AS SN_FBBC
        FROM isat_report.susy_bbmod_r WHERE  productName = 'Flexi Baseband Sub-Module FBBC' GROUP BY mrbts,productName ;

			Drop table if EXISTS isat_report.susy_tempFBBA;
        create TABLE isat_report.susy_tempFBBA(
			`xdate` DATE NOT NULL
			,`mrbts` MEDIUMINT(9) NULL DEFAULT NULL
			,`productName` VARCHAR(50) NULL DEFAULT NULL
			,`FBBA` MEDIUMINT(9) NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS))
			SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FBBA',group_concat(serialNumber separator "-") AS SN_FBBA
        FROM isat_report.susy_bbmod_r WHERE  productName = 'BB Extension Outdoor Sub-Module FBBA' GROUP BY mrbts,productName;


			Drop table if EXISTS isat_report.susy_tempABIA;
        create TABLE isat_report.susy_tempABIA(
			`xdate` DATE NOT NULL
			,`mrbts` MEDIUMINT(9) NULL DEFAULT NULL
			,`productName` VARCHAR(50) NULL DEFAULT NULL
			,`ABIA` MEDIUMINT(9) NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS))
			SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'ABIA',group_concat(serialNumber separator "-") AS SN_ABIA
        FROM isat_report.susy_bbmod_r WHERE  productName = 'ABIA AirScale Capacity' GROUP BY mrbts,productName;

			Drop table if EXISTS isat_report.susy_tempASIA;
        create TABLE isat_report.susy_tempASIA(
			`xdate` DATE NOT NULL
			,`mrbts` MEDIUMINT(9) NULL DEFAULT NULL
			,`productName` VARCHAR(50) NULL DEFAULT NULL
			,`ASIA` MEDIUMINT(9) NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS))
			SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'ASIA',group_concat(serialNumber separator "-") AS SN_ASIA
        FROM isat_report.susy_smod_r WHERE  productName = 'ASIA AirScale Common' GROUP BY mrbts,productName;

			Drop table if EXISTS isat_report.susy_tempUNKNOWN;
        create TABLE isat_report.susy_tempUNKNOWN(
			`xdate` DATE NOT NULL
			,`mrbts` MEDIUMINT(9) NULL DEFAULT NULL
			,`productName` VARCHAR(50) NULL DEFAULT NULL
			,`UNKNOWN` MEDIUMINT(9) NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS))
			SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'UNKNOWN',group_concat(serialNumber separator "-") AS SN_UNKNOWN
        FROM isat_report.susy_bbmod_r WHERE  productName = 'UNKNOWN' GROUP BY mrbts,productName;

			Drop table if EXISTS isat_report.susy_tempFWGM;
        create TABLE isat_report.susy_tempFWGM(
			`xdate` DATE NOT NULL
			,`mrbts` MEDIUMINT(9) NULL DEFAULT NULL
			,`productName` VARCHAR(50) NULL DEFAULT NULL
			,`FWGM` MEDIUMINT(9) NULL DEFAULT NULL,
			PRIMARY KEY (MRBTS))
			SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FWGM',group_concat(serialNumber separator "-") AS SN_FWGM
        FROM isat_report.susy_smod_r WHERE  productName = 'FWGM' GROUP BY mrbts,productName ;




			Drop table if EXISTS isat_report.susy_hwi_smod;
        create TABLE isat_report.susy_hwi_smod(
	`SITE_ID` VARCHAR(54) NOT NULL,
	`MRBTS` INT(11) NOT NULL,
	`FSMF` BIGINT(21) NOT NULL DEFAULT '0',
	`FW2GEA` BIGINT(21) NOT NULL DEFAULT '0',
	`FW2EA` BIGINT(21) NOT NULL DEFAULT '0',
	`FWGM` BIGINT(21) NOT NULL DEFAULT '0',
	`FBBC` BIGINT(21) NOT NULL DEFAULT '0',
	`FBBA` BIGINT(21) NOT NULL DEFAULT '0',
	`ABIA` BIGINT(21) NOT NULL DEFAULT '0',
	`ASIA` BIGINT(21) NOT NULL DEFAULT '0',
	`UNKNOWN` BIGINT(21) NOT NULL DEFAULT '0',
	`remark` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
    `Serial_number_Smod` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
   `Serial_number_Bbmod` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
	`wbtsId` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
	`bscId` MEDIUMINT(8) UNSIGNED NULL DEFAULT NULL,
	`bcfId` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
	`Position_Left` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
	`Position_Right` VARCHAR(222) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
		PRIMARY KEY (SITE_ID,MRBTS))
        SELECT a.Site_id_susy as SITE_ID, a.MRBTS
        ,ifnull(FSMF,0) 'FSMF'
        ,ifnull(FW2GEA,0) 'FW2GEA'
        ,ifnull(FW2EA,0) 'FW2EA'
        ,ifnull(FWGM,0) 'FWGM'
        ,ifnull(FBBC,0) 'FBBC'
        ,ifnull(FBBA,0) 'FBBA'
        ,ifnull(ABIA,0) 'ABIA'
        ,ifnull(ASIA,0) 'ASIA'
        ,ifnull(UNKNOWN,0) 'UNKNOWN'

		  ,concat(ifnull(concat(FSMF,"_FSMF "),""),ifnull(concat(FW2GEA,"_FW2GEA "),""),ifnull(concat(FWGM,"_FWGM "),"")
        ,ifnull(concat(FW2EA,"_FW2EA "),""),ifnull(concat(FBBC,"_FBBC "),""),ifnull(concat(FBBA,"_FBBA "),"")
		  ,ifnull(concat(ASIA,"_ASIA "),""),ifnull(concat(ABIA,"_ABIA "),""),ifnull(concat(UNKNOWN,"_UNKNOWN "),"")) AS 'remark'
           ,concat(ifnull(concat(SN_FSMF ,"_FSMF "),""),ifnull(concat(SN_FW2GEA ,"_FW2GEA "),""),ifnull(concat(SN_FW2EA ,"_FW2EA "),""),ifnull(concat(SN_ASIA ,"_ASIA "),""),ifnull(concat(SN_UNKNOWN ,"_UNKNOWN "),""),ifnull(concat(SN_FWGM ,"_FWGM "),"")) AS Serial_number_Smod
		  ,concat(ifnull(concat(SN_FBBC ,"_FBBC "),""),ifnull(concat(SN_FBBA ,"_FBBA "),""),ifnull(concat(SN_ABIA ,"_ABIA "),"")) AS Serial_number_Bbmod

        ,e.wbtsId
        ,f.bscId
        ,f.bcfId

		  FROM
        isat_report.susy_profile4g a
        left JOIN isat_report.susy_tempfsmf b
        ON a.mrbts = b.mrbts
        left JOIN isat_report.susy_tempFW2GEA c
        ON a.mrbts = c.mrbts
        left JOIN isat_report.susy_tempFW2EA d
        ON a.mrbts = d.mrbts
        LEFT JOIN isat_report.susy_relation3g e
        ON a.mrbts = e.MRBTS
        LEFT JOIN isat_report.susy_temp2g4g f
      	ON a.mrbts = f.MRBTS
         left JOIN isat_report.susy_tempFBBC g
        ON a.mrbts = g.mrbts
        left JOIN isat_report.susy_tempFBBA h
        ON a.mrbts = h.mrbts
        left JOIN isat_report.susy_tempABIA i
        ON a.mrbts = i.mrbts
        left JOIN isat_report.susy_tempUNKNOWN j
        ON a.mrbts = j.mrbts
		  left JOIN isat_report.susy_tempASIA k
        ON a.mrbts = k.mrbts
        left JOIN isat_report.susy_tempFWGM l
        ON a.mrbts = l.mrbts

		  WHERE IFNULL(a.Site_id_susy,'')<>''
        GROUP BY a.Site_id_susy,a.mrbts;

        Drop table if EXISTS isat_report.susy_relation3g;
        Drop table if EXISTS isat_report.susy_bbmod_r;
        Drop table if EXISTS isat_report.susy_smod_r;

			Drop table if EXISTS isat_report.susy_temp2g4g;

			Drop table if EXISTS isat_report.susy_tempfsmf;
			Drop table if EXISTS isat_report.susy_tempFW2GEA;
			Drop table if EXISTS isat_report.susy_tempFW2EA;
			Drop table if EXISTS isat_report.susy_tempFBBC;
			Drop table if EXISTS isat_report.susy_tempFBBA;
        	Drop table if EXISTS isat_report.susy_tempABIA;
        	Drop table if EXISTS isat_report.susy_tempASIA;
        	Drop table if EXISTS isat_report.susy_tempUNKNOWN;
        	Drop table if EXISTS isat_report.susy_tempFWGM;
        """
    elif Request == "hwi_update_4":
        sqlscript_query = """
        Drop table if EXISTS isat_report.susy_trmod_r;
        create TABLE isat_report.susy_trmod_r (
        		`oss` VARCHAR(100) NOT NULL,
        	`xdate` DATE NOT NULL,
        	`distName` VARCHAR(100) NOT NULL,
        	`MRBTS` MEDIUMINT(9) NULL DEFAULT NULL,
        	`EQM` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`APEQM` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`CABINET` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`TRMOD` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`configDN` VARCHAR(50) NULL DEFAULT NULL,
        	`operationalState` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`productCode` VARCHAR(50) NULL DEFAULT NULL,
        	`productName` VARCHAR(50) NULL DEFAULT NULL,
        	`serialNumber` VARCHAR(50) NULL DEFAULT NULL,
        	`class` VARCHAR(100) NULL DEFAULT NULL,
        	`defaults` VARCHAR(50) NULL DEFAULT NULL,
        	`filename` VARCHAR(255) NULL DEFAULT NULL,
        	`availabilityStatus` TINYINT(3) UNSIGNED NULL DEFAULT NULL,
        	`distidentifier` VARCHAR(100) NULL DEFAULT NULL,
                	PRIMARY KEY (distName))

        	SELECT oss,xdate,distName,MRBTS
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"EQM")+4,INSTR(a.configDN,"APEQM")-INSTR(a.configDN,"EQM")-5),EQM_R) AS EQM
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"APEQM")+6,INSTR(a.configDN,"CABINET")-INSTR(a.configDN,"APEQM")-7),APEQM_R) AS APEQM
        	,ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"CABINET")+8,INSTR(a.configDN,"TRMOD")-INSTR(a.configDN,"CABINET")-9),CABINET_R) AS CABINET
        	, ifnull(SUBSTRING(a.configDN,INSTR(a.configDN,"TRMOD")+6,1),TRMOD_R) AS TRMOD
        	,configDN,operationalState,productCode,productName,serialNumber,class,defaults,filename,availabilityStatus,distidentifier
        	FROM isat_cm.trmod_r a
        	WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """'  GROUP BY configDN,distName;

       TRUNCATE isat_report.susy_hwi_tmod;
        REPLACE into isat_report.susy_hwi_tmod
        SELECT
        a.Site_id_susy AS  SITE_ID
        ,a.mrbts
        ,FTIF
        ,concat(FTIF,"_FTIF") AS 'remark'
        ,ifnull(concat(SN_FTIF ,"_FTIF "),"") AS Serial_number_trmod
        FROM
        isat_report.susy_profile4g a
        left JOIN
        (SELECT xdate,mrbts,productName,COUNT(DISTINCT serialNumber) AS 'FTIF',group_concat(serialNumber separator "-") AS SN_FTIF
        FROM isat_report.susy_trmod_r WHERE  productName = 'FTIF' GROUP BY mrbts,productName) b
		  ON a.mrbts = b.mrbts
        WHERE FTIF IS NOT null
        GROUP BY a.Site_id_susy,a.mrbts;
        Drop table if EXISTS isat_report.susy_trmod_r;"""
    elif Request == "hwi_update_5":
        sqlscript_query = """
        Drop table if EXISTS  isat_report.temp_sranserialnumber;
        CREATE TABLE isat_report.temp_sranserialnumber(
        	`serialNumber` VARCHAR(50) NOT NULL DEFAULT '',
        	PRIMARY KEY (serialNumber))
        	(SELECT serialNumber FROM isat_cm.smod_r WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """' and serialNumber is not null GROUP BY serialNumber)
			  union
			 (SELECT serialNumber FROM isat_cm.bbmod_r WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """' and serialNumber is not null  GROUP BY serialNumber)
			  union
			 (SELECT serialNumber FROM isat_cm.rmod_r WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """' and serialNumber is not null GROUP BY serialNumber)
			 union
			 (SELECT serialNumber FROM isat_cm.trmod_r WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """' and serialNumber is not null  GROUP BY serialNumber);

Drop table if EXISTS  isat_report.temp_submodule;
        CREATE TABLE isat_report.temp_submodule(
        	`xdate` DATE NOT NULL,
        	`distname` VARCHAR(100) NOT NULL,
        	`unitType` VARCHAR(50) NULL DEFAULT NULL,
        	`module` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
        	`unit_type` VARCHAR(50) NULL DEFAULT NULL,
        	`RNCIDBSCID` VARCHAR(10) NOT NULL DEFAULT '',
        	`WBTSBCFID` VARCHAR(10) NOT NULL DEFAULT '',
        	`mrbts` MEDIUMINT(9) NULL DEFAULT NULL,
        	`serialNumber` VARCHAR(50) NOT NULL DEFAULT '',
        	 PRIMARY KEY (RNCIDBSCID,WBTSBCFID,mrbts,distname))
        SELECT xdate,distname,unitType,module
        ,REPLACE(unitType,"CORE_","") AS "unit_type"
        ,SUBSTRING(distname, LOCATE('RNC',distname )+4,LOCATE('/',distname,LOCATE('RNC',distname )) - LOCATE('RNC',distname )-4) AS 'RNCIDBSCID'
        ,SUBSTRING(distname, LOCATE('WBTS',distname )+5,LOCATE('/',distname,LOCATE('WBTS',distname )) - LOCATE('WBTS',distname )-5) AS 'WBTSBCFID'
        ,mrbts,a.serialNumber
        FROM isat_cm.submodule a
		  left Join isat_report.temp_sranserialnumber b ON a.serialNumber = b.serialNumber WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """'
		  AND b.serialNumber is null AND
         (unitType  like '%ESMC%' or unitType like '%ESMB%' or unitType like '%FSMF%' or unitType like '%ESMA%'
         or unitType like '%ESEA%' or unitType like '%FBBC%' or unitType like '%FBBA%' or unitType like '%FSME%'
        or unitType like '%FSMD%' or unitType like '%FRGU%' or unitType like '%FRGP%' or unitType like '%FRGF%'
        or unitType like '%FXDB%' or unitType like '%ARGA%'or unitType like '%FXDA%' or unitType like '%FRGT%' or unitType like '%FXDJ%'
        or unitType like '%FRGC%' or unitType like '%FRGD%' or unitType like '%FXJB%' or unitType like '%FXED%'
        or unitType like '%FXEA%' or unitType like '%FXEB%' or unitType like '%EXDB%' or unitType like '%EXDA%'
        or unitType like '%EXGB%' or unitType like '%EXGA%' or unitType like '%FHDB%' or unitType like '%ECU%'
        or unitType like '%FDU%' or unitType like '%CUG%' or unitType like '%GCU%' or unitType like '%FIQB%'
        or unitType like '%FTIF%' or unitType like '%FIPA%' or unitType like '%FIQA%' or unitType like '%FTIB%'
        or unitType like '%FTHA%' or unitType like '%FTIA%' or unitType like '%FWGM%' or unitType like '%AREA%'
        or unitType like '%FR2EA%' or unitType like '%FR2EC%' or unitType like '%FR2GA%' or unitType like '%AHDA%' or unitType like '%FHDB%'
        ) GROUP BY xdate,mrbts,distname;


        Drop table if EXISTS  isat_report.temp_module;
        CREATE TABLE isat_report.temp_module(
        	`xdate` DATE NOT NULL,
        	`distname` VARCHAR(100) NOT NULL,
        	`userlabel` VARCHAR(50) NULL DEFAULT NULL,
        	`module` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
        	`user_label` VARCHAR(50) NULL DEFAULT NULL,
        	`RNCIDBSCID` VARCHAR(10) NOT NULL DEFAULT '',
        	`WBTSBCFID` VARCHAR(10) NOT NULL DEFAULT '',
        	`mrbts` MEDIUMINT(9) NULL DEFAULT NULL,
        	`serialNumber` VARCHAR(50) NOT NULL DEFAULT '',
        	 PRIMARY KEY (RNCIDBSCID,WBTSBCFID,mrbts,distname))

        SELECT xdate,distname,userlabel,module
        ,REPLACE(userlabel,"CORE_","") AS "user_label"
        ,SUBSTRING(distname, LOCATE('RNC',distname )+4,LOCATE('/',distname,LOCATE('RNC',distname )) - LOCATE('RNC',distname )-4) AS 'RNCIDBSCID'
        ,SUBSTRING(distname, LOCATE('WBTS',distname )+5,LOCATE('/',distname,LOCATE('WBTS',distname )) - LOCATE('WBTS',distname )-5) AS 'WBTSBCFID'
        ,mrbts,a.serialNumber
        FROM isat_cm.module a
		  left Join isat_report.temp_sranserialnumber b ON a.serialNumber = b.serialNumber
		  WHERE xdate =   '""" + hwitime.strftime("%Y-%m-%d") + """' AND b.serialNumber is null AND
         (userlabel  like '%ESMC%' or userlabel like '%ESMB%' or userlabel like '%FSMF%' or userlabel like '%ESMA%'
         or userlabel like '%ESEA%' or userlabel like '%FBBC%' or userlabel like '%FBBA%' or userlabel like '%FSME%'
        or userlabel like '%FSMD%' or userlabel like '%FRGU%' or userlabel like '%FRGP%' or userlabel like '%FRGF%'
        or userlabel like '%FXDB%' or userlabel like '%ARGA%' or userlabel like '%FXDA%' or userlabel like '%FRGT%' or userlabel like '%FXDJ%'
        or userlabel like '%FRGC%' or userlabel like '%FRGD%' or userlabel like '%FXJB%' or userlabel like '%FXED%'
        or userlabel like '%FXEA%' or userlabel like '%FXEB%' or userlabel like '%EXDB%' or userlabel like '%EXDA%'
        or userlabel like '%EXGB%' or userlabel like '%EXGA%' or userlabel like '%FHDB%' or userlabel like '%ECU%'
        or userlabel like '%FDU%' or userlabel like '%CUG%' or userlabel like '%GCU%' or userlabel like '%FIQB%'
        or userlabel like '%FTIF%' or userlabel like '%FIPA%' or userlabel like '%FIQA%' or userlabel like '%FTIB%'
        or userlabel like '%FTHA%' or userlabel like '%FTIA%' or userlabel like '%FWGM%' or userlabel like '%AREA%'
        or userlabel like '%FR2GA%' or userlabel like '%FR2EC%' or userlabel like '%FR2EA%' or userlabel like '%AHDA%' or userlabel like '%FHDB%'
        )  GROUP BY xdate,mrbts,distname;


        	Drop table if EXISTS  isat_report.temp_module_submodule;
        CREATE TABLE isat_report.temp_module_submodule(
        	`xdate` DATE NOT NULL,
        	`distname` VARCHAR(100) NOT NULL,
        	`unit_type` VARCHAR(50) NULL DEFAULT NULL,
        	`RNCIDBSCID` int(50) NOT NULL,
        	`WBTSBCFID` int(50) NOT NULL,
        	`mrbts` int(50) NOT NULL,
        	`serialNumber` VARCHAR(50) NOT NULL,
        	 PRIMARY KEY (RNCIDBSCID,WBTSBCFID,mrbts,serialNumber))
        	  SELECT xdate,distname,unit_type,RNCIDBSCID,WBTSBCFID,mrbts,serialNumber
            FROM((
            SELECT a.xdate,a.distname,a.user_label AS unit_type,a.RNCIDBSCID,a.WBTSBCFID,a.mrbts,serialNumber
            FROM isat_report.temp_module a WHERE serialNumber IS not null) UNION

            		 (
            SELECT b.xdate,b.distname,b.unit_type,b.RNCIDBSCID,b.WBTSBCFID,b.mrbts,serialNumber
            FROM isat_report.temp_submodule b WHERE serialNumber is not null
            		)) c
            GROUP BY RNCIDBSCID,WBTSBCFID,mrbts,serialNumber ;


         Drop table if EXISTS  isat_report.susy_hwi_submodule;
        CREATE TABLE isat_report.susy_hwi_submodule(

        `RNCIDBSCID` int(50) NOT NULL,
          `WBTSBCFID` int(50) NOT NULL,
          `mrbts` int(50) NOT NULL,
          `unit_type` varchar(50) NOT NULL,
          `count` bigint(21) NOT NULL DEFAULT '0',
          `module` varchar(50) NOT NULL DEFAULT '0',
          `type` varchar(50) NOT NULL DEFAULT '0',
          PRIMARY KEY (`RNCIDBSCID`,`WBTSBCFID`,`mrbts`,`unit_type`))
         (SELECT
        if(a.RNCIDBSCID="",0,a.RNCIDBSCID) AS 'RNCIDBSCID'
        ,if(a.WBTSBCFID="",0,a.WBTSBCFID) AS 'WBTSBCFID'
        ,ifnull(a.mrbts,0) AS 'mrbts'
        ,a.unit_type
        ,COUNT(a.unit_type) AS 'count'
        ,CONCAT(COUNT(a.unit_type),'_',a.unit_type) AS 'module'
        ,if(unit_type  like '%ESMC%'or unit_type like '%ESMB%'
        or unit_type like '%FSMF%'or unit_type like '%ESMA%'or unit_type like '%ESEA%'or unit_type like '%FBBC%'or unit_type like '%FBBA%'
        or unit_type like '%FSME%' or unit_type like '%FSMD%' OR (unit_type like '%FWGM%' AND unit_type not like '%FRGM%') ,'smod',
        if(unit_type like '%FIQB%'or unit_type like '%FTIF%' or unit_type like '%FIPA%'or unit_type like '%FIQA%'
        or unit_type like '%FTIB%'or unit_type like '%FTHA%'
        or unit_type like '%FTIA%','tmod','rmod')
        ) as 'type'
        FROM isat_report.temp_module_submodule a GROUP BY RNCIDBSCID,WBTSBCFID,mrbts,serialNumber
        )

        UNION

        (
        SELECT bsc AS 'RNCIDBSCID',bcf AS 'WBTSBCFID',0 AS 'mrbts',SUBSTRING(unit,1, LOCATE('_',unit)-1) AS 'unit_type',COUNT(bcf) AS 'COUNT' ,CONCAT(COUNT(bcf),"_",SUBSTRING(unit,1, LOCATE('_',unit)-1)) AS 'module'
        ,if(unit  like '%ESMC%'or unit like '%ESMB%'
        or unit like '%FSMF%'or unit like '%ESMA%'or unit like '%ESEA%'or unit like '%FBBC%'or unit like '%FBBA%'or unit like '%FSME%'
        or unit like '%FSMD%','smod',
        if(unit like '%FIQB%'or unit like '%FTIF%'
        or unit like '%FIPA%'or unit like '%FIQA%'or unit like '%FTIB%'or unit like '%FTHA%'
        or unit like '%FTIA%','tmod','rmod')
        ) as 'type'

        FROM isat_cm.unit a left Join isat_report.temp_sranserialnumber b ON a.serialNumber = b.serialNumber
         WHERE xdate =  '""" + hwitime.strftime("%Y-%m-%d") + """' AND b.serialNumber is null
        AND (unit  like '%ESMC%'or unit like '%ESMB%'
        or unit like '%FSMF%'or unit like '%ESMA%'or unit like '%ESEA%'or unit like '%FBBC%'or unit like '%FBBA%'or unit like '%FSME%'
        or unit like '%FSMD%'or unit like '%FRGU%'or unit like '%FRGP%'or unit like '%FRGF%' or unit like '%FXDB%' or unit like '%ARGA%' or unit like '%FXDA%'
        or unit like '%FRGT%'or unit like '%FXDJ%'or unit like '%FRGC%'or unit like '%FRGD%'
        or unit like '%FXJB%'or unit like '%FXED%'or unit like '%FXEA%'
        or unit like '%FXEB%'or unit like '%EXDB%'or unit like '%EXDA%'or unit like '%EXGB%'
        or unit like '%EXGA%'or unit like '%FHDB%'or unit like '%ECU%'or unit like '%FDU%'
        or unit like '%CUG%'or unit like '%GCU%'or unit like '%FIQB%'or unit like '%FTIF%'
        or unit like '%FIPA%'or unit like '%FIQA%'or unit like '%FTIB%'or unit like '%FTHA%'
        or unit like '%FTIA%' or unit like '%AREA%' or unit like '%FR2EA%' or unit like '%FR2EC%' or unit like '%FR2GA%'
        or unit like '%AHDA%' or unit like '%FHDB%'
        )
         GROUP BY bsc,bcf,SUBSTRING(unit,1, LOCATE('_',unit)-1)
        );
        Drop table if EXISTS  isat_report.temp_module_submodule;
        Drop table if EXISTS  isat_report.temp_submodule;
        Drop table if EXISTS  isat_report.temp_module;
        Drop table if EXISTS  isat_report.temp_sranserialnumber;

        """
    elif Request == "hwi_update_6":
        sqlscript_query = """
        TRUNCATE isat_report.susy_hwi_nonsran_submodule;
        REPLACE into isat_report.susy_hwi_nonsran_submodule
        SELECT xx.site_id,xx.bscidGSM,xx.bcfidGSM,xx.bscidDCS,xx.bcfidDCS,xx.RNCBAND900,xx.WBTSBAND900,xx.RNCBAND2100,xx.WBTSBAND2100,xx.MRBTS900,xx.MRBTS1800,xx.MRBTS2100
        ,a.RMOD_G900
        ,b.RMOD_G1800
        ,c.RMOD_U900
        ,d.RMOD_U2100
        ,m.RMOD_L900
        ,n.RMOD_L1800
        ,o.RMOD_L2100

        ,e.SMOD_G900
        ,f.SMOD_G1800
        ,g.SMOD_U900
        ,h.SMOD_U2100
        ,p.SMOD_L900
        ,q.SMOD_L1800
        ,r.SMOD_L2100

        ,i.TMOD_G900
        ,j.TMOD_G1800
        ,k.TMOD_U900
        ,l.TMOD_U2100
        ,s.TMOD_L900
        ,t.TMOD_L1800
        ,u.TMOD_L2100
        FROM isat_report.susy_band_bw xx
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'RMOD_G900'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.bscidGSM = b.RNCIDBSCID and a.bcfidGSM = b.WBTSBCFID
        WHERE b.`type` = 'rmod' GROUP BY a.site_id
        ) a ON xx.site_id = a.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'RMOD_G1800'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.bscidDCS = b.RNCIDBSCID AND a.bcfidDCS = b.WBTSBCFID
        WHERE b.`type` = 'rmod' GROUP BY a.site_id
        ) b ON xx.site_id = b.site_id

        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'RMOD_U900'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.RNCBAND900 = b.RNCIDBSCID AND a.WBTSBAND900 = b.WBTSBCFID
        WHERE b.`type` = 'rmod' GROUP BY a.site_id
        ) c ON xx.site_id = c.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'RMOD_U2100'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.RNCBAND2100 = b.RNCIDBSCID AND a.WBTSBAND2100 = b.WBTSBCFID
        WHERE b.`type` = 'rmod' GROUP BY a.site_id
        ) d ON xx.site_id = d.site_id

        LEFT JOIN (
        SELECT a.site_id,GROUP_CONCAT(DISTINCT b.module ORDER BY b.unit_type DESC SEPARATOR ' ' ) AS 'SMOD_G900'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.bscidGSM = b.RNCIDBSCID and a.bcfidGSM = b.WBTSBCFID
        WHERE b.`type` = 'smod' GROUP BY a.site_id
        ) e ON xx.site_id = e.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module  ORDER BY b.unit_type DESC SEPARATOR ' ') AS 'SMOD_G1800'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.bscidDCS = b.RNCIDBSCID AND a.bcfidDCS = b.WBTSBCFID
        WHERE b.`type` = 'smod' GROUP BY a.site_id
        ) f ON xx.site_id = f.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module  ORDER BY b.unit_type DESC SEPARATOR ' ' ) AS 'SMOD_U900'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.RNCBAND900 = b.RNCIDBSCID AND a.WBTSBAND900 = b.WBTSBCFID
        WHERE b.`type` = 'smod' GROUP BY a.site_id
        ) g ON xx.site_id = g.site_id
        LEFT JOIN (
        SELECT a.site_id,GROUP_CONCAT(DISTINCT b.module   ORDER BY b.unit_type DESC SEPARATOR ' ' ) AS 'SMOD_U2100'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.RNCBAND2100 = b.RNCIDBSCID AND a.WBTSBAND2100 = b.WBTSBCFID
        WHERE b.`type` = 'smod' GROUP BY a.site_id
        ) h ON xx.site_id = h.site_id

        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'TMOD_G900'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.bscidGSM = b.RNCIDBSCID and a.bcfidGSM = b.WBTSBCFID
        WHERE b.`type` = 'tmod' GROUP BY a.site_id
        ) i ON xx.site_id = i.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'TMOD_G1800'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.bscidDCS = b.RNCIDBSCID AND a.bcfidDCS = b.WBTSBCFID
        WHERE b.`type` = 'tmod' GROUP BY a.site_id
        ) j ON xx.site_id = j.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'TMOD_U900'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.RNCBAND900 = b.RNCIDBSCID AND a.WBTSBAND900 = b.WBTSBCFID
        WHERE b.`type` = 'tmod' GROUP BY a.site_id
        ) k ON xx.site_id = k.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'TMOD_U2100'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.RNCBAND2100 = b.RNCIDBSCID AND a.WBTSBAND2100 = b.WBTSBCFID
        WHERE b.`type` = 'tmod' GROUP BY a.site_id
        ) l ON xx.site_id = l.site_id

        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'RMOD_L900'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.MRBTS900 = b.mrbts
        WHERE b.`type` = 'rmod' GROUP BY a.site_id
        ) m ON xx.site_id = m.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'RMOD_L1800'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.MRBTS1800 = b.mrbts
        WHERE b.`type` = 'rmod' GROUP BY a.site_id
        ) n ON xx.site_id = n.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'RMOD_L2100'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.MRBTS2100 = b.mrbts
        WHERE b.`type` = 'rmod' GROUP BY a.site_id
        ) o ON xx.site_id = o.site_id

        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module  ORDER BY b.unit_type DESC SEPARATOR ' ' ) AS 'SMOD_L900'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.MRBTS900 = b.mrbts
        WHERE b.`type` = 'smod' GROUP BY a.site_id
        ) p ON xx.site_id = p.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module  ORDER BY b.unit_type DESC SEPARATOR ' ') AS 'SMOD_L1800'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.MRBTS1800 = b.mrbts
        WHERE b.`type` = 'smod' GROUP BY a.site_id
        ) q ON xx.site_id = q.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module  ORDER BY b.unit_type DESC SEPARATOR ' ') AS 'SMOD_L2100'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.MRBTS2100 = b.mrbts
        WHERE b.`type` = 'smod' GROUP BY a.site_id
        ) r ON xx.site_id = r.site_id

        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'TMOD_L900'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.MRBTS900 = b.mrbts
        WHERE b.`type` = 'tmod' GROUP BY a.site_id
        ) s ON xx.site_id = s.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'TMOD_L1800'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.MRBTS1800 = b.mrbts
        WHERE b.`type` = 'tmod' GROUP BY a.site_id
        ) t ON xx.site_id = t.site_id
        LEFT JOIN (
        SELECT a.site_id ,GROUP_CONCAT(DISTINCT b.module SEPARATOR ' ') AS 'TMOD_L2100'
        FROM isat_report.susy_band_bw a JOIN isat_report.susy_hwi_submodule b ON a.MRBTS2100 = b.mrbts
        WHERE b.`type` = 'tmod' GROUP BY a.site_id
        ) u ON xx.site_id = u.site_id

        """
    elif Request == "hwi_update_7":
        sqlscript_query = """
        TRUNCATE isat_report.susy_hwi_3guarfcn;
        REPLACE into isat_report.susy_hwi_3guarfcn
        SELECT aa.Site_id_susy as SITE_ID,aa.RNC, aa.WBTS

        , if(sum(UARFCN_3) is NULL
		  		,CONCAT(if(sum(UARFCN_1) is NULL, '',concat(sum(UARFCN_1),"_"))
		  		,if(sum(UARFCN_2) is NULL, '',sum(UARFCN_2)))
		  ,CONCAT(if(sum(UARFCN_1) is NULL, '',concat(sum(UARFCN_1),"_"))
		  ,if(sum(UARFCN_2) is NULL, '',concat(sum(UARFCN_2),"_"))
		  ,sum(UARFCN_3))) 'UARFCN_900'

        , if(sum(UARFCN_6) is NULL
		  			,CONCAT(if(sum(UARFCN_4) is NULL, '',concat(sum(UARFCN_4),"_"))
		  			,if(sum(UARFCN_5) is NULL, '',sum(UARFCN_5)))
		  ,CONCAT(if(sum(UARFCN_4) is NULL, '',concat(sum(UARFCN_4),"_"))
		  ,if(sum(UARFCN_5) is NULL, '',concat(sum(UARFCN_5),"_" ))
		  ,sum(UARFCN_6))) 'UARFCN_2100'

		,if(GROUP_CONCAT( c.AdminCellState3 SEPARATOR ',') is NULL
				,CONCAT(if(GROUP_CONCAT(a.AdminCellState1 SEPARATOR ',') is NULL,'',concat(GROUP_CONCAT(a.AdminCellState1 SEPARATOR ','),"_"))
		 		,if(GROUP_CONCAT( b.AdminCellState2 SEPARATOR ',') is NULL,'',GROUP_CONCAT( b.AdminCellState2 SEPARATOR ',')))
		,CONCAT(if(GROUP_CONCAT(a.AdminCellState1 SEPARATOR ',') is NULL,'',concat(GROUP_CONCAT(a.AdminCellState1 SEPARATOR ','),"_"))
		 ,if(GROUP_CONCAT( b.AdminCellState2 SEPARATOR ',') is NULL,'',concat(GROUP_CONCAT( b.AdminCellState2 SEPARATOR ','),"_"))
		 ,GROUP_CONCAT( c.AdminCellState3 SEPARATOR ',')))  AS 'AdminCellState_900'

		,if(GROUP_CONCAT( f.AdminCellState3 SEPARATOR ',')  is NULL
				,CONCAT(if( GROUP_CONCAT( d.AdminCellState1 SEPARATOR ',') is NULL, '',concat(GROUP_CONCAT( d.AdminCellState1 SEPARATOR ','),"_"))
				,if( GROUP_CONCAT( e.AdminCellState2 SEPARATOR ',') is NULL, '',GROUP_CONCAT( e.AdminCellState2 SEPARATOR ',')))
		,CONCAT(if( GROUP_CONCAT( d.AdminCellState1 SEPARATOR ',') is NULL, '',concat(GROUP_CONCAT( d.AdminCellState1 SEPARATOR ','),"_"))
		,if( GROUP_CONCAT( e.AdminCellState2 SEPARATOR ',') is NULL, '',concat(GROUP_CONCAT( e.AdminCellState2 SEPARATOR ','),"_"))
		,GROUP_CONCAT( f.AdminCellState3 SEPARATOR ','))) 'AdminCellState_2100'


        ,if( GROUP_CONCAT( c.HosRemark SEPARATOR ',')  is NULL
        		,CONCAT(if( GROUP_CONCAT( a.HosRemark SEPARATOR ',')is NULL, '',concat(GROUP_CONCAT( a.HosRemark SEPARATOR ','),"_"))
		  		,if( GROUP_CONCAT( b.HosRemark SEPARATOR ',')  is NULL, '',GROUP_CONCAT( b.HosRemark SEPARATOR ',')))
		  ,CONCAT(if( GROUP_CONCAT( a.HosRemark SEPARATOR ',')is NULL, '',concat(GROUP_CONCAT( a.HosRemark SEPARATOR ','),"_"))
		  ,if( GROUP_CONCAT( b.HosRemark SEPARATOR ',')  is NULL, '',concat(GROUP_CONCAT( b.HosRemark SEPARATOR ','),"_"))
		  ,GROUP_CONCAT( c.HosRemark SEPARATOR ','))) 'HosRemark_900'

        ,if(GROUP_CONCAT( f.HosRemark SEPARATOR ',')  is NULL
        		,CONCAT(if(GROUP_CONCAT( d.HosRemark SEPARATOR ',')  is NULL, '',concat(GROUP_CONCAT( d.HosRemark SEPARATOR ','),"_"))
		  		,if(GROUP_CONCAT( e.HosRemark SEPARATOR ',')  is NULL, '',GROUP_CONCAT( e.HosRemark SEPARATOR ',')))
		  ,CONCAT(if(GROUP_CONCAT( d.HosRemark SEPARATOR ',')  is NULL, '',concat(GROUP_CONCAT( d.HosRemark SEPARATOR ','),"_"))
		  ,if(GROUP_CONCAT( e.HosRemark SEPARATOR ',')  is NULL, '',concat(GROUP_CONCAT( e.HosRemark SEPARATOR ','),"_"))
		  ,GROUP_CONCAT( f.HosRemark SEPARATOR ','))) 'HosRemark_2100'
        ,aa.SBTS_status

        FROM isat_report.susy_profile3g aa
        LEFT JOIN (
        SELECT a.Site_id_susy as SITE_ID, a.RNC, a.WBTS, a.WCEL, b.SectorID
        , count(b.UARFCN) 'UARFCN_1',GROUP_CONCAT(a.AdminCellState SEPARATOR ',') 'AdminCellState1'
        ,GROUP_CONCAT(if(( INSTR(a.NAME,'_A1') or INSTR(a.NAME,'_A2') or INSTR(a.NAME,'_A3') or INSTR(a.NAME,'_B1') or INSTR(a.NAME,'_B2') or INSTR(a.NAME,'_B3') or INSTR(a.NAME,'_A4') or INSTR(a.NAME,'_A5') or INSTR(a.NAME,'_A6') or INSTR(a.NAME,'_B4') or INSTR(a.NAME,'_B5') or INSTR(a.NAME,'_B6'))<>0 ,"HOS","n") SEPARATOR ',') as HosRemark
        FROM isat_report.susy_profile3g a
        JOIN isat_cm.wcel b ON a.RNC = b.RNC AND a.WBTS = b.WBTS and a.WCEL = b.WCEL
        WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (b.SectorID = 1 OR b.SectorID = 4 )
        AND (b.UARFCN = 3013 or b.UARFCN = 3037)
        GROUP BY a.Site_id_susy,a.RNC, a.WBTS,b.UARFCN ) a ON aa.Site_id_susy = a.SITE_ID and aa.RNC = a.RNC AND aa.WBTS = a.WBTS AND aa.WCEL = a.WCEL


			LEFT JOIN (
        SELECT a.Site_id_susy as SITE_ID, a.RNC, a.WBTS, a.WCEL, b.SectorID
        , count(b.UARFCN) 'UARFCN_2',GROUP_CONCAT(a.AdminCellState SEPARATOR ',') 'AdminCellState2'
        ,GROUP_CONCAT(if(( INSTR(a.NAME,'_A1') or INSTR(a.NAME,'_A2') or INSTR(a.NAME,'_A3') or INSTR(a.NAME,'_B1') or INSTR(a.NAME,'_B2') or INSTR(a.NAME,'_B3') or INSTR(a.NAME,'_A4') or INSTR(a.NAME,'_A5') or INSTR(a.NAME,'_A6') or INSTR(a.NAME,'_B4') or INSTR(a.NAME,'_B5') or INSTR(a.NAME,'_B6'))<>0 ,"HOS","n") SEPARATOR ',') as HosRemark
        FROM isat_report.susy_profile3g a
        JOIN isat_cm.wcel b ON a.RNC = b.RNC AND a.WBTS = b.WBTS and a.WCEL = b.WCEL
        WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (b.SectorID = 2 OR b.SectorID = 5 )
        AND (b.UARFCN = 3013 or b.UARFCN = 3037)
        GROUP BY a.Site_id_susy,a.RNC, a.WBTS,b.UARFCN ) b ON aa.Site_id_susy =b.SITE_ID and aa.RNC = b.RNC AND aa.WBTS = b.WBTS AND aa.WCEL = b.WCEL

        LEFT JOIN (
        SELECT a.Site_id_susy as SITE_ID, a.RNC, a.WBTS, a.WCEL, b.SectorID
        , count(b.UARFCN) 'UARFCN_3',GROUP_CONCAT(a.AdminCellState SEPARATOR ',') 'AdminCellState3'
        ,GROUP_CONCAT(if(( INSTR(a.NAME,'_A1') or INSTR(a.NAME,'_A2') or INSTR(a.NAME,'_A3') or INSTR(a.NAME,'_B1') or INSTR(a.NAME,'_B2') or INSTR(a.NAME,'_B3') or INSTR(a.NAME,'_A4') or INSTR(a.NAME,'_A5') or INSTR(a.NAME,'_A6') or INSTR(a.NAME,'_B4') or INSTR(a.NAME,'_B5') or INSTR(a.NAME,'_B6'))<>0 ,"HOS","n") SEPARATOR ',') as HosRemark
        FROM isat_report.susy_profile3g a
        JOIN isat_cm.wcel b ON a.RNC = b.RNC AND a.WBTS = b.WBTS and a.WCEL = b.WCEL
        WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (b.SectorID = 3 OR b.SectorID = 6 )
        AND (b.UARFCN = 3013 or b.UARFCN = 3037)
        GROUP BY a.Site_id_susy,a.RNC, a.WBTS,b.UARFCN ) c ON aa.Site_id_susy = c.SITE_ID and aa.RNC = c.RNC AND aa.WBTS = c.WBTS AND aa.WCEL = c.WCEL

        LEFT JOIN (
        SELECT a.Site_id_susy as SITE_ID, a.RNC, a.WBTS, a.WCEL, b.SectorID
        , count(b.UARFCN) 'UARFCN_4',GROUP_CONCAT(a.AdminCellState SEPARATOR ',') 'AdminCellState1'
        ,GROUP_CONCAT(if(( INSTR(a.NAME,'_A1') or INSTR(a.NAME,'_A2') or INSTR(a.NAME,'_A3') or INSTR(a.NAME,'_B1') or INSTR(a.NAME,'_B2') or INSTR(a.NAME,'_B3') or INSTR(a.NAME,'_A4') or INSTR(a.NAME,'_A5') or INSTR(a.NAME,'_A6') or INSTR(a.NAME,'_B4') or INSTR(a.NAME,'_B5') or INSTR(a.NAME,'_B6'))<>0 ,"HOS","n") SEPARATOR ',') as HosRemark
        FROM isat_report.susy_profile3g a
        JOIN isat_cm.wcel b ON a.RNC = b.RNC AND a.WBTS = b.WBTS and a.WCEL = b.WCEL
        WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (b.SectorID = 1 OR b.SectorID = 4 )
        AND (b.UARFCN = 10838 or b.UARFCN = 10813)
        GROUP BY a.Site_id_susy,a.RNC, a.WBTS,b.UARFCN ) d ON aa.Site_id_susy = d.SITE_ID and aa.RNC = d.RNC AND aa.WBTS = d.WBTS AND aa.WCEL = d.WCEL

        LEFT JOIN (
        SELECT a.Site_id_susy as SITE_ID, a.RNC, a.WBTS, a.WCEL, b.SectorID
        , count(b.UARFCN) 'UARFCN_5',GROUP_CONCAT(a.AdminCellState SEPARATOR ',') 'AdminCellState2'
        ,GROUP_CONCAT(if(( INSTR(a.NAME,'_A1') or INSTR(a.NAME,'_A2') or INSTR(a.NAME,'_A3') or INSTR(a.NAME,'_B1') or INSTR(a.NAME,'_B2') or INSTR(a.NAME,'_B3') or INSTR(a.NAME,'_A4') or INSTR(a.NAME,'_A5') or INSTR(a.NAME,'_A6') or INSTR(a.NAME,'_B4') or INSTR(a.NAME,'_B5') or INSTR(a.NAME,'_B6'))<>0 ,"HOS","n") SEPARATOR ',') as HosRemark
        FROM isat_report.susy_profile3g a
        JOIN isat_cm.wcel b ON a.RNC = b.RNC AND a.WBTS = b.WBTS and a.WCEL = b.WCEL
        WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (b.SectorID = 2 OR b.SectorID = 5 )
        AND (b.UARFCN = 10838 or b.UARFCN = 10813)
        GROUP BY a.Site_id_susy,a.RNC, a.WBTS,b.UARFCN ) e ON aa.Site_id_susy = e.SITE_ID and aa.RNC = e.RNC AND aa.WBTS = e.WBTS AND aa.WCEL = e.WCEL

        LEFT JOIN (
        SELECT a.Site_id_susy as SITE_ID, a.RNC, a.WBTS, a.WCEL, b.SectorID
        , count(b.UARFCN) 'UARFCN_6',GROUP_CONCAT(a.AdminCellState SEPARATOR ',') 'AdminCellState3'
        ,GROUP_CONCAT(if(( INSTR(a.NAME,'_A1') or INSTR(a.NAME,'_A2') or INSTR(a.NAME,'_A3') or INSTR(a.NAME,'_B1') or INSTR(a.NAME,'_B2') or INSTR(a.NAME,'_B3') or INSTR(a.NAME,'_A4') or INSTR(a.NAME,'_A5') or INSTR(a.NAME,'_A6') or INSTR(a.NAME,'_B4') or INSTR(a.NAME,'_B5') or INSTR(a.NAME,'_B6'))<>0 ,"HOS","n") SEPARATOR ',') as HosRemark
        FROM isat_report.susy_profile3g a
        JOIN isat_cm.wcel b ON a.RNC = b.RNC AND a.WBTS = b.WBTS and a.WCEL = b.WCEL
        WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (b.SectorID = 3 OR b.SectorID = 6 )
        AND (b.UARFCN = 10838 or b.UARFCN = 10813)
        GROUP BY a.Site_id_susy,a.RNC, a.WBTS,b.UARFCN ) f ON aa.Site_id_susy = f.SITE_ID and aa.RNC = f.RNC AND aa.WBTS = f.WBTS AND aa.WCEL = f.WCEL


        WHERE aa.Site_id_susy IS NOT NULL

        GROUP BY  aa.Site_id_susy,aa.RNC, aa.WBTS
        """
    elif Request == "hwi_update_8":
        sqlscript_query = """
        TRUNCATE isat_report.susy_hwi_2gtrx;
		REPLACE into isat_report.susy_hwi_2gtrx

        SELECT
        aa.Site_id_susy as SITE_ID, aa.bsc, aa.bcf

        ,if(sum(GTRX_Count_3) is NULL
        		,CONCAT(if(sum(GTRX_Count_1) is NULL,'',concat(sum(GTRX_Count_1),"_"))
		  		,if(sum(GTRX_Count_2) is NULL,'',sum(GTRX_Count_2 )))
		  ,CONCAT(if(sum(GTRX_Count_1) is NULL,'',concat(sum(GTRX_Count_1),"_"))
		  ,if(sum(GTRX_Count_2) is NULL,'',concat(sum(GTRX_Count_2),"_" ))
		  ,sum(GTRX_Count_3))
		  ) AS TRX_GSM

        ,if(sum(DTRX_Count_3) is NULL
        		,CONCAT(if(sum(DTRX_Count_1) is NULL,'',concat(sum(DTRX_Count_1),"_"))
		  		,if(sum(DTRX_Count_2) is NULL,'',sum(DTRX_Count_2)))
		  ,CONCAT(if(sum(DTRX_Count_1) is NULL,'',concat(sum(DTRX_Count_1),"_"))
		  ,if(sum(DTRX_Count_2) is NULL,'',concat(sum(DTRX_Count_2),"_"))
		  ,sum(DTRX_Count_3))
		  ) AS TRX_DCS

        ,if(SUM(c.adminState_3) is NULL
        		,CONCAT(if(SUM(a.adminState_1) is NULL,'',concat(sum(a.adminState_1),"_"))
		  		,if(sum(b.adminState_2) is NULL,'',SUM(b.adminState_2)))
		  ,CONCAT(if(SUM(a.adminState_1) is NULL,'',concat(sum(a.adminState_1),"_"))
		  ,if(sum(b.adminState_2) is NULL,'',concat(SUM(b.adminState_2),"_"))
		  ,SUM(c.adminState_3))
		  ) AS adminState_GSM

         ,if(SUM(f.adminState_3) is NULL
         		,CONCAT(if(SUM(d.adminState_1) is NULL,'',concat(sum(d.adminState_1),"_" ))
					,if(sum(e.adminState_2) is NULL,'',SUM(e.adminState_2)))
			,CONCAT(if(SUM(d.adminState_1) is NULL,'',concat(sum(d.adminState_1),"_" ))
			,if(sum(e.adminState_2) is NULL,'',concat(SUM(e.adminState_2),"_"))
			,SUM(f.adminState_3))
			) AS adminState_DCS

         ,aa.SBTS_status
        FROM isat_report.susy_profile2g aa
        LEFT JOIN (
        SELECT  a.Site_id_susy as SITE_ID, a.bsc, a.bcf, a.bts, a.Sector_ID 'Sector_ID_1',a.Sector_ID
        ,COUNT(b.TRX) 'GTRX_Count_1',c.frequencyBandInUse,a.adminState 'adminState_1'
        from isat_report.susy_profile2g a
        JOIN isat_cm.trx b  ON a.bsc = b.BSC AND a.bcf = b.BCF AND a.bts = b.BTS
        JOIN isat_cm.bts c ON b.xdate = c.xdate AND b.bsc = c.bsc AND b.bcf = c.BCF AND b.bts = c.BTS
        WHERE b.xdate ='""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (a.Sector_ID = 1 OR a.Sector_ID = 4 OR a.Sector_ID = 0 OR a.Sector_ID = 7)
        AND c.frequencyBandInUse = 0
        GROUP BY  a.bsc, a.bcf, a.bts ) a on   aa.bsc = a.bsc AND aa.bcf = a.bcf AND aa.bts = a.bts

        LEFT JOIN (
        SELECT  a.Site_id_susy as SITE_ID, a.bsc, a.bcf, a.bts, a.Sector_ID 'Sector_ID_2',a.Sector_ID
        ,COUNT(b.TRX) 'GTRX_Count_2',c.frequencyBandInUse,a.adminState 'adminState_2'
        from isat_report.susy_profile2g a
        JOIN isat_cm.trx b  ON a.bsc = b.BSC AND a.bcf = b.BCF AND a.bts = b.BTS
        JOIN isat_cm.bts c ON b.xdate = c.xdate AND b.bsc = c.bsc AND b.bcf = c.BCF AND b.bts = c.BTS
        WHERE b.xdate ='""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (a.Sector_ID = 2 OR a.Sector_ID = 5 OR a.Sector_ID = 8)
        AND c.frequencyBandInUse = 0
        GROUP BY a.bsc, a.bcf, a.bts ) b ON  aa.bsc = b.bsc AND aa.bcf = b.bcf AND aa.bts = b.bts

        LEFT JOIN (
        SELECT  a.Site_id_susy as SITE_ID, a.bsc, a.bcf, a.bts, a.Sector_ID 'Sector_ID_3',a.Sector_ID
        ,COUNT(b.TRX) 'GTRX_Count_3',c.frequencyBandInUse,a.adminState 'adminState_3'
        from isat_report.susy_profile2g a
        JOIN isat_cm.trx b  ON a.bsc = b.BSC AND a.bcf = b.BCF AND a.bts = b.BTS
        JOIN isat_cm.bts c ON b.xdate = c.xdate AND b.bsc = c.bsc AND b.bcf = c.BCF AND b.bts = c.BTS
        WHERE b.xdate ='""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (a.Sector_ID = 3 OR a.Sector_ID = 6 OR a.Sector_ID = 9)
        AND c.frequencyBandInUse = 0
        GROUP BY  a.bsc, a.bcf, a.bts ) c ON  aa.bsc = c.bsc AND aa.bcf = c.bcf AND aa.bts = c.bts


        LEFT JOIN (
        SELECT  a.Site_id_susy as SITE_ID, a.bsc, a.bcf, a.bts, a.Sector_ID 'Sector_ID_1',a.Sector_ID
        ,COUNT(b.TRX) 'DTRX_Count_1',c.frequencyBandInUse,a.adminState 'adminState_1'
        from isat_report.susy_profile2g a
        JOIN isat_cm.trx b  ON a.bsc = b.BSC AND a.bcf = b.BCF AND a.bts = b.BTS
        JOIN isat_cm.bts c ON b.xdate = c.xdate AND b.bsc = c.bsc AND b.bcf = c.BCF AND b.bts = c.BTS
        WHERE b.xdate ='""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (a.Sector_ID = 1 OR a.Sector_ID = 4 OR a.Sector_ID = 7 OR a.Sector_ID = 0)
        AND c.frequencyBandInUse = 1
        GROUP BY  a.bsc, a.bcf, a.bts ) d on   aa.bsc = d.bsc AND aa.bcf = d.bcf AND aa.bts = d.bts

        LEFT JOIN (
        SELECT  a.Site_id_susy as SITE_ID, a.bsc, a.bcf, a.bts, a.Sector_ID 'Sector_ID_2',a.Sector_ID
        ,COUNT(b.TRX) 'DTRX_Count_2',c.frequencyBandInUse,a.adminState 'adminState_2'
        from isat_report.susy_profile2g a
        JOIN isat_cm.trx b  ON a.bsc = b.BSC AND a.bcf = b.BCF AND a.bts = b.BTS
        JOIN isat_cm.bts c ON b.xdate = c.xdate AND b.bsc = c.bsc AND b.bcf = c.BCF AND b.bts = c.BTS
        WHERE b.xdate ='""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (a.Sector_ID = 2 OR a.Sector_ID = 5 OR a.Sector_ID = 8)
        AND c.frequencyBandInUse = 1
        GROUP BY a.bsc, a.bcf, a.bts ) e ON  aa.bsc = e.bsc AND aa.bcf = e.bcf AND aa.bts = e.bts

        LEFT JOIN (
        SELECT  a.Site_id_susy as SITE_ID, a.bsc, a.bcf, a.bts, a.Sector_ID 'Sector_ID_3',a.Sector_ID
        ,COUNT(b.TRX) 'DTRX_Count_3',c.frequencyBandInUse,a.adminState 'adminState_3'
        from isat_report.susy_profile2g a
        JOIN isat_cm.trx b  ON a.bsc = b.BSC AND a.bcf = b.BCF AND a.bts = b.BTS
        JOIN isat_cm.bts c ON b.xdate = c.xdate AND b.bsc = c.bsc AND b.bcf = c.BCF AND b.bts = c.BTS
        WHERE b.xdate ='""" + hwitime.strftime("%Y-%m-%d") + """'
        AND (a.Sector_ID = 3 OR a.Sector_ID = 6 OR a.Sector_ID = 9)
        AND c.frequencyBandInUse = 1
        GROUP BY  a.bsc, a.bcf, a.bts ) f ON  aa.bsc = f.bsc AND aa.bcf = f.bcf AND aa.bts = f.bts

        WHERE aa.Site_id_susy  IS NOT NULL

        GROUP BY  aa.Site_id_susy,aa.bsc, aa.bcf"""
    elif Request == "hwi_update_9":
        sqlscript_query = """
        Drop table if EXISTS isat_report.susy_temp_anttype;
        create TABLE isat_report.susy_temp_anttype
		  (`Site_id` VARCHAR(54) NOT NULL DEFAULT '',
		  `mrbts` INT(11) NOT NULL,
        	`antenna` VARCHAR(54) NULL DEFAULT NULL,
        	`BAND` CHAR(50) NULL DEFAULT NULL,
        	PRIMARY KEY (mrbts))
        	SELECT b.Site_id_susy AS Site_id,a.mrbts,GROUP_CONCAT(antModel SEPARATOR ",") AS antenna,b.Band
			FROM (SELECT mrbts,antModel FROM isat_cm.retu a WHERE xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' AND antModel <> ""  GROUP BY mrbts,antModel) a
			JOIN (SELECT * from isat_report.susy_profile4G GROUP BY mrbts) b ON a.MRBTS = b.mrbts
			GROUP BY mrbts;


        Drop table if EXISTS isat_report.susy_temp_gsm;
        create TABLE isat_report.susy_temp_gsm (
        `Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        `name` VARCHAR(50) NULL DEFAULT NULL,
        `bscidGSM` INT(11) NULL DEFAULT '0',
        `bcfidGSM` SMALLINT(5) NULL DEFAULT '0',
        `GSM_COLOCATEDidentifyer` SMALLINT(5) NULL DEFAULT NULL,
        `Site_2g` VARCHAR(54) NULL DEFAULT NULL,
        PRIMARY KEY (Site_id_susy,bscidGSM,bcfidGSM))
        SELECT b.Site_id_susy,c.name,b.bsc AS bscidGSM,b.bcf AS bcfidGSM,b.bcf_susy 'GSM_COLOCATEDidentifyer', b.SBTS_status 'GSM_SBTS_status',b.Site_id_2G AS  Site_2g
        FROM isat_report.susysiteidlist a
        LEFT JOIN isat_report.susy_profile2G b on a.SITE_ID = b.Site_id_susy
        JOIN isat_cm.bcf c ON c.BSC = b.bsc AND c.BCF = b.bcf
        WHERE b.BAND = 900 AND c.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        GROUP BY b.Site_id_susy;

        Drop table if EXISTS isat_report.susy_temp_dcs;
        create TABLE isat_report.susy_temp_dcs (
        `Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        `name` VARCHAR(50) NULL DEFAULT NULL,
        `bscidDCS` INT(11) NULL DEFAULT '0',
        `bcfidDCS` SMALLINT(5) NULL DEFAULT '0',
        `DCS_COLOCATEDidentifyer` SMALLINT(5) NULL DEFAULT NULL,
        `DCS_SBTS_status` CHAR(50) NULL DEFAULT NULL,
        `Site_2g` VARCHAR(54) NULL DEFAULT NULL,
        PRIMARY KEY (Site_id_susy,bscidDCS,bcfidDCS))
        SELECT b.Site_id_susy,c.name,b.bsc AS bscidDCS,b.bcf AS bcfidDCS,b.bcf_susy 'DCS_COLOCATEDidentifyer',b.SBTS_status 'DCS_SBTS_status',b.Site_id_2G AS  Site_2g
        FROM isat_report.susysiteidlist a
        LEFT JOIN isat_report.susy_profile2G b on a.SITE_ID = b.Site_id_susy
        JOIN isat_cm.bcf c ON c.BSC = b.bsc AND c.BCF = b.bcf
        WHERE b.BAND = 1800 AND c.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        GROUP BY b.Site_id_susy;


        Drop table if EXISTS isat_report.susy_temp_u2100;
        create TABLE isat_report.susy_temp_u2100 (
        `Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`name` VARCHAR(50) NULL DEFAULT NULL,
        	`RNCBAND2100` SMALLINT(6) NULL,
        	`WBTSBAND2100` SMALLINT(6) NULL,
        	`U2100_COLOCATEDidentifyer` SMALLINT(6) NULL DEFAULT NULL,
        	`U2100_SBTS_status` CHAR(50) NULL DEFAULT NULL,
        	`Site_3g` VARCHAR(54) NULL DEFAULT NULL,
        PRIMARY KEY (Site_id_susy,RNCBAND2100,WBTSBAND2100))
        SELECT c.Site_id_susy,d.name,c.RNC 'RNCBAND2100',c.WBTS 'WBTSBAND2100',c.WBTS_susy 'U2100_COLOCATEDidentifyer', c.SBTS_status 'U2100_SBTS_status',c. Site_id_3G AS Site_3g
        FROM isat_report.susysiteidlist a
        LEFT JOIN isat_report.susy_profile3G c on a.SITE_ID = c.Site_id_susy
        JOIN isat_cm.wbts d ON d.RNC = c.RNC AND d.wbts = c.wbts
        WHERE C.BAND = 2100 AND d.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        GROUP BY c.Site_id_susy;


        Drop table if EXISTS isat_report.susy_temp_u900;
            create TABLE isat_report.susy_temp_u900(
		  `Site_id_susy` VARCHAR(54) NULL DEFAULT NULL,
        	`name` VARCHAR(50) NULL DEFAULT NULL,
        	`RNCBAND900` SMALLINT(6) NULL,
        	`WBTSBAND900` SMALLINT(6) NULL,
        	`U900_COLOCATEDidentifyer` SMALLINT(6) NULL DEFAULT NULL,
        	`U900_SBTS_status` CHAR(50) NULL DEFAULT NULL,
        	`Site_3g` VARCHAR(54) NULL DEFAULT NULL,
        PRIMARY KEY (Site_id_susy,RNCBAND900,WBTSBAND900))
        SELECT c.Site_id_susy,d.name,c.RNC 'RNCBAND900',c.WBTS 'WBTSBAND900',c.WBTS_susy 'U900_COLOCATEDidentifyer', c.SBTS_status 'U900_SBTS_status',c. Site_id_3G AS Site_3g
        FROM isat_report.susysiteidlist a
        LEFT JOIN isat_report.susy_profile3G c on a.SITE_ID = c.Site_id_susy
        JOIN isat_cm.wbts d ON d.RNC = c.RNC AND d.wbts = c.wbts
        WHERE c.BAND = 900 AND d.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """' GROUP BY c.Site_id_susy;


        Drop table if EXISTS isat_report.susy_temp_l900;
            create TABLE isat_report.susy_temp_l900(
            `Site_id_susy` VARCHAR(54) NULL DEFAULT '',
        	`name` VARCHAR(50) NULL DEFAULT NULL,
        	`MRBTS900` INT(11) NULL,
        	`LNBTS900` INT(11) NULL,
        	`BW_L900` DOUBLE(17,0) NULL DEFAULT NULL,
        	`version_L900` VARCHAR(50) NULL DEFAULT NULL,
        	`ANTENA` CHAR(50) NULL DEFAULT NULL,
        	`L900_COLOCATEDidentifyer` INT(11) NULL,
        PRIMARY KEY (Site_id_susy,MRBTS900,LNBTS900))
        SELECT d.Site_id_susy,i.name, d.MRBTS 'MRBTS900',d.MRBTS 'LNBTS900', d.BW 'BW_L900',h.version 'version_L900',d.ANTENA,d.mrbts_susy 'L900_COLOCATEDidentifyer'
        FROM isat_report.susysiteidlist a
        LEFT JOIN isat_report.susy_profile4G d ON a.SITE_ID = d.Site_id_susy
        JOIN isat_cm.mrbts h on d.MRBTS = h.MRBTS
        JOIN isat_cm.lnbts i on h.MRBTS = i.MRBTS AND h.xdate = i.xdate
        WHERE d.BAND = 900
        AND h.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        GROUP BY d.Site_id_susy;



        Drop table if EXISTS isat_report.susy_temp_l2100;
            create TABLE isat_report.susy_temp_l2100(
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT '',
        	`name` VARCHAR(50) NULL DEFAULT NULL,
        	`MRBTS2100` INT(11) NULL,
        	`LNBTS2100` INT(11) NULL,
        	`BW_L2100` DOUBLE(17,0) NULL DEFAULT NULL,
        	`version_L2100` VARCHAR(50) NULL DEFAULT NULL,
        	`ANTENA` CHAR(50) NULL DEFAULT NULL,
        	`L2100_COLOCATEDidentifyer` INT(11) NULL,
        PRIMARY KEY (Site_id_susy,MRBTS2100,LNBTS2100))
        SELECT d.Site_id_susy,i.name, d.MRBTS 'MRBTS2100',d.MRBTS 'LNBTS2100', d.BW 'BW_L2100',h.version 'version_L2100',d.ANTENA,d.mrbts_susy 'L2100_COLOCATEDidentifyer'
        FROM isat_report.susysiteidlist a
        LEFT JOIN isat_report.susy_profile4G d ON a.SITE_ID = d.Site_id_susy
        JOIN isat_cm.mrbts h on d.MRBTS = h.MRBTS
        JOIN isat_cm.lnbts i on h.MRBTS = i.MRBTS AND h.xdate = i.xdate
        WHERE d.BAND = 2100
        AND h.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        GROUP BY d.Site_id_susy;


        Drop table if EXISTS isat_report.susy_temp_l1800;
                create TABLE isat_report.susy_temp_l1800 (
        	`Site_id_susy` VARCHAR(54) NULL DEFAULT '',
        	`name` VARCHAR(50) NULL DEFAULT NULL,
        	`MRBTS1800` INT(11) NULL,
        	`LNBTS1800` INT(11) NULL,
        	`BW_L1800` DOUBLE(17,0) NULL DEFAULT NULL,
        	`version_L1800` VARCHAR(50) NULL DEFAULT NULL,
        	`ANTENA` CHAR(50) NULL DEFAULT NULL,
        	`L1800_COLOCATEDidentifyer` INT(11) NULL,
        PRIMARY KEY (Site_id_susy,MRBTS1800,LNBTS1800))
        SELECT d.Site_id_susy,i.name, d.MRBTS 'MRBTS1800',d.MRBTS 'LNBTS1800', d.BW 'BW_L1800',h.version 'version_L1800',d.ANTENA,d.mrbts_susy 'L1800_COLOCATEDidentifyer'
        FROM isat_report.susysiteidlist a
        LEFT JOIN isat_report.susy_profile4G d ON a.SITE_ID = d.Site_id_susy
        JOIN isat_cm.mrbts h on d.MRBTS = h.MRBTS
        JOIN isat_cm.lnbts i on h.MRBTS = i.MRBTS AND h.xdate = i.xdate
        WHERE d.BAND = 1800
        AND h.xdate = '""" + hwitime.strftime("%Y-%m-%d") + """'
        GROUP BY d.Site_id_susy;

        TRUNCATE isat_report.susy_band_bw;
        REPLACE INTO isat_report.susy_band_bw
        select
        cc.oss
        ,cc.SITE_ID as site_id
        ,if(a.Site_2g = b.Site_2g,a.Site_2g,concat(a.Site_2g,"_",b.Site_2g)) AS siteid2G
        ,if(c.Site_3g = d.Site_3g,c.Site_3g,concat(c.Site_3g,"_",d.Site_3g)) AS siteid3G
        ,bscidGSM
        ,bcfidGSM
        ,a.GSM_COLOCATEDidentifyer
        ,a.name AS 'GSMname'
        ,bscidDCS
        ,bcfidDCS
        ,b.DCS_COLOCATEDidentifyer
        ,b.name AS 'DCSname'
        ,RNCBAND900
        ,WBTSBAND900
        ,c.U900_COLOCATEDidentifyer
        ,c.name AS 'U900name'
        ,RNCBAND2100
        ,WBTSBAND2100
        ,d.U2100_COLOCATEDidentifyer
        ,d.name AS 'U2100name'
        ,MRBTS900
        ,MRBTS1800
        ,MRBTS2100
        ,e.L900_COLOCATEDidentifyer
        ,g.L1800_COLOCATEDidentifyer
        ,f.L2100_COLOCATEDidentifyer
        ,e.name AS 'L900name'
        ,g.name AS 'L1800name'
        ,f.name AS 'L2100name'
        ,BW_L900
        ,BW_L2100
        ,BW_L1800
        ,GSM_SBTS_status
        ,DCS_SBTS_status
        ,U900_SBTS_status
        ,U2100_SBTS_status
        ,version_L900
        ,version_L1800
        ,version_L2100
        ,e.ANTENA AS "antConfig_L900"
		,g.ANTENA AS "antConfig_L1800"
		,f.ANTENA AS "antConfig_L2100"
		,antTypeL900
		,antTypeL1800
		,antTypeL2100
        FROM isat_report.susysiteidlist cc

        LEFT JOIN isat_report.susy_temp_gsm a ON cc.site_id = a.Site_id_susy

        left JOIN isat_report.susy_temp_dcs b ON cc.site_id = b.Site_id_susy

        left JOIN isat_report.susy_temp_u900 c ON cc.site_id = c.Site_id_susy

        left JOIN isat_report.susy_temp_u2100 d ON cc.site_id = d.Site_id_susy

        left JOIN isat_report.susy_temp_l900 e ON cc.SITE_ID = e.Site_id_susy

        left JOIN isat_report.susy_temp_l2100 f ON cc.SITE_ID = f.Site_id_susy

        LEFT JOIN isat_report.susy_temp_l1800 g ON cc.SITE_ID = g.Site_id_susy

			LEFT JOIN (SELECT Site_id,antenna AS antTypeL900 From isat_report.susy_temp_anttype WHERE band = 900 GROUP BY Site_id) h ON cc.SITE_ID = h.Site_id
			LEFT JOIN (SELECT Site_id,antenna AS antTypeL1800 From isat_report.susy_temp_anttype WHERE band = 1800 GROUP BY Site_id) i ON cc.SITE_ID = i.Site_id
			LEFT JOIN (SELECT Site_id,antenna AS antTypeL2100 From isat_report.susy_temp_anttype WHERE band = 2100 GROUP BY Site_id) j ON cc.SITE_ID = j.Site_id
        WHERE cc.SITE_ID <> ""
        GROUP BY cc.SITE_ID ;

        Drop table if EXISTS isat_report.susy_temp_anttype;
        Drop table if EXISTS isat_report.susy_temp_gsm;
        Drop table if EXISTS isat_report.susy_temp_dcs;
        Drop table if EXISTS isat_report.susy_temp_u900;
        Drop table if EXISTS isat_report.susy_temp_u2100;
        Drop table if EXISTS isat_report.susy_temp_l900;
        Drop table if EXISTS isat_report.susy_temp_l1800;
        Drop table if EXISTS isat_report.susy_temp_l2100;
        """

    #hourly bot chat===========================================
    elif Request == "lnbts_list":
        sqlscript_query = """
        select MRBTS from isat_cm.lnbts where (xdate = '""" + todayminus8hour.strftime("%Y-%m-%d") + """' or xdate = '""" + twodaysago.strftime("%Y-%m-%d") + """') and  MRBTS is not null group by MRBTS"""
    elif Request == "4G_MC_perf":
        sqlscript_query ="""SELECT a.xDate,a.xHour,a.MICRO_CLUSTER,a.Band
        ,round(100*(SUM(a.`Cell_Availability num`)/SUM(a.`Cell_Availability denum`)),2) AS `Cell_Availability`
        ,round(100*((SUM(a.`CSSR num1`)/SUM(a.`CSSR denum1`))*(SUM(a.`CSSR num2`)/SUM(a.`CSSR denum2`))*(SUM(a.`CSSR num3`)/SUM(a.`CSSR denum3`))),2) AS `CSSR`
        ,round(100*(SUM(a.`S1_Establisment_SR num`)/SUM(a.`S1_Establisment_SR denum`)),2) AS `S1_Establisment_SR`
        ,round(100*(SUM(a.`E-RAB_Drop num`)/SUM(a.`E-RAB_Drop denum`)),2) AS `E-RAB_Drop`
        ,round(100*(SUM(a.`Intra_HO num`)/SUM(a.`Intra_HO denum`)),2) AS `Intra_HO`
        ,round(100*(SUM(a.`Inter_Freq_HO num`)/SUM(a.`Inter_Freq_HO denum`)),2) AS `Inter_Freq_HO`
        ,ROUND(SUM(a.`Total_Payload(MBytes)`),2) AS `Total_Payload(MBytes)`
        ,round((SUM(a.`LTE_IP_User_Throughput_DL num`)/SUM(a.`LTE_IP_User_Throughput_DL denum`)),2) AS `LTE_IP_User_Throughput_DL`
        ,Sum(ERAB_rel_user_inactivity) as 'ERAB_rel_user_inactivity'
        ,Sum(Radio_Connection_with_UE_lost) as 'Radio_Connection_with_UE_lost'
        ,Sum(ERAB_rel_UE_redirected) as 'ERAB_rel_UE_redirected'
        ,Sum(ERAB_rel_EUTRAN) as 'ERAB_rel_EUTRAN'
        ,Sum(ERAB_rel_GBR_congestion) as 'ERAB_rel_GBR_congestion'
        ,Sum(ERAB_rel_fail_Ho_Completion) as 'ERAB_rel_fail_Ho_Completion'
        ,Sum(ERAB_insuf_transport_resource) as 'ERAB_insuf_transport_resource'
        ,SUM(ERAB_rel_exp_HO_Guard_Time) AS 'ERAB_rel_exp_HO_Guard_Time'
        ,sum(Transp_Res_Unavailable) as 'Transp_Res_Unavailable'
        ,sum(Number_UEs_active_2_Scells) as 'Number_UEs_active_2_Scells'
        FROM isat_report.susy_4Gperfcell_2 a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "4G_subMC_perf":
        sqlscript_query ="""SELECT a.xDate,a.xHour,a.Subscluster,a.Band
        ,round(100*(SUM(a.`Cell_Availability num`)/SUM(a.`Cell_Availability denum`)),2) AS `Cell_Availability`
        ,round(100*((SUM(a.`CSSR num1`)/SUM(a.`CSSR denum1`))*(SUM(a.`CSSR num2`)/SUM(a.`CSSR denum2`))*(SUM(a.`CSSR num3`)/SUM(a.`CSSR denum3`))),2) AS `CSSR`
        ,round(100*(SUM(a.`S1_Establisment_SR num`)/SUM(a.`S1_Establisment_SR denum`)),2) AS `S1_Establisment_SR`
        ,round(100*(SUM(a.`E-RAB_Drop num`)/SUM(a.`E-RAB_Drop denum`)),2) AS `E-RAB_Drop`
        ,round(100*(SUM(a.`Intra_HO num`)/SUM(a.`Intra_HO denum`)),2) AS `Intra_HO`
        ,round(100*(SUM(a.`Inter_Freq_HO num`)/SUM(a.`Inter_Freq_HO denum`)),2) AS `Inter_Freq_HO`
        ,ROUND(SUM(a.`Total_Payload(MBytes)`),2) AS `Total_Payload(MBytes)`
        ,round((SUM(a.`LTE_IP_User_Throughput_DL num`)/SUM(a.`LTE_IP_User_Throughput_DL denum`)),2) AS `LTE_IP_User_Throughput_DL`
        ,Sum(ERAB_rel_user_inactivity) as 'ERAB_rel_user_inactivity'
        ,Sum(Radio_Connection_with_UE_lost) as 'Radio_Connection_with_UE_lost'
        ,Sum(ERAB_rel_UE_redirected) as 'ERAB_rel_UE_redirected'
        ,Sum(ERAB_rel_EUTRAN) as 'ERAB_rel_EUTRAN'
        ,Sum(ERAB_rel_GBR_congestion) as 'ERAB_rel_GBR_congestion'
        ,Sum(ERAB_rel_fail_Ho_Completion) as 'ERAB_rel_fail_Ho_Completion'
        ,Sum(ERAB_insuf_transport_resource) as 'ERAB_insuf_transport_resource'
        ,SUM(ERAB_rel_exp_HO_Guard_Time) AS 'ERAB_rel_exp_HO_Guard_Time'
        ,sum(Transp_Res_Unavailable) as 'Transp_Res_Unavailable'
        ,sum(Number_UEs_active_2_Scells) as 'Number_UEs_active_2_Scells'
        FROM isat_report.susy_4Gperfcell_2 a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "REGION":
        sqlscript_query ="""SELECT a.xDate,a.xHour,a.REGION,a.Band
        ,round(100*(SUM(a.`Cell_Availability num`)/SUM(a.`Cell_Availability denum`)),2) AS `Cell_Availability`
        ,round(100*((SUM(a.`CSSR num1`)/SUM(a.`CSSR denum1`))*(SUM(a.`CSSR num2`)/SUM(a.`CSSR denum2`))*(SUM(a.`CSSR num3`)/SUM(a.`CSSR denum3`))),2) AS `CSSR`
        ,round(100*(SUM(a.`S1_Establisment_SR num`)/SUM(a.`S1_Establisment_SR denum`)),2) AS `S1_Establisment_SR`
        ,round(100*(SUM(a.`E-RAB_Drop num`)/SUM(a.`E-RAB_Drop denum`)),2) AS `E-RAB_Drop`
        ,round(100*(SUM(a.`Intra_HO num`)/SUM(a.`Intra_HO denum`)),2) AS `Intra_HO`
        ,round(100*(SUM(a.`Inter_Freq_HO num`)/SUM(a.`Inter_Freq_HO denum`)),2) AS `Inter_Freq_HO`
        ,ROUND(SUM(a.`Total_Payload(MBytes)`),2) AS `Total_Payload(MBytes)`
        ,round((SUM(a.`LTE_IP_User_Throughput_DL num`)/SUM(a.`LTE_IP_User_Throughput_DL denum`)),2) AS `LTE_IP_User_Throughput_DL`
        ,Sum(ERAB_rel_user_inactivity) as 'ERAB_rel_user_inactivity'
        ,Sum(Radio_Connection_with_UE_lost) as 'Radio_Connection_with_UE_lost'
        ,Sum(ERAB_rel_UE_redirected) as 'ERAB_rel_UE_redirected'
        ,Sum(ERAB_rel_EUTRAN) as 'ERAB_rel_EUTRAN'
        ,Sum(ERAB_rel_GBR_congestion) as 'ERAB_rel_GBR_congestion'
        ,Sum(ERAB_rel_fail_Ho_Completion) as 'ERAB_rel_fail_Ho_Completion'
        ,Sum(ERAB_insuf_transport_resource) as 'ERAB_insuf_transport_resource'
        ,SUM(ERAB_rel_exp_HO_Guard_Time) AS 'ERAB_rel_exp_HO_Guard_Time'
        ,sum(Transp_Res_Unavailable) as 'Transp_Res_Unavailable'
        ,sum(Number_UEs_active_2_Scells) as 'Number_UEs_active_2_Scells'
        FROM isat_report.susy_4Gperfcell_2 a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "CLUSTER2b":
        sqlscript_query ="""SELECT a.xDate,a.xHour,a.CLUSTER2b as cluster ,a.Band
        ,round(100*(SUM(a.`Cell_Availability num`)/SUM(a.`Cell_Availability denum`)),2) AS `Cell_Availability`
        ,round(100*((SUM(a.`CSSR num1`)/SUM(a.`CSSR denum1`))*(SUM(a.`CSSR num2`)/SUM(a.`CSSR denum2`))*(SUM(a.`CSSR num3`)/SUM(a.`CSSR denum3`))),2) AS `CSSR`
        ,round(100*(SUM(a.`E-RAB_Drop num`)/SUM(a.`E-RAB_Drop denum`)),2) AS `E-RAB_Drop`
        ,round(100*(SUM(a.`S1_Establisment_SR num`)/SUM(a.`S1_Establisment_SR denum`)),2) AS `S1_Establisment_SR`
        ,round(100*(SUM(a.`Intra_HO num`)/SUM(a.`Intra_HO denum`)),2) AS `Intra_HO`
        ,round(100*(SUM(a.`Inter_Freq_HO num`)/SUM(a.`Inter_Freq_HO denum`)),2) AS `Inter_Freq_HO`
        ,ROUND(SUM(a.`Total_Payload(MBytes)`),2) AS `Total_Payload(MBytes)`
        ,round((SUM(a.`LTE_IP_User_Throughput_DL num`)/SUM(a.`LTE_IP_User_Throughput_DL denum`)),2) AS `LTE_IP_User_Throughput_DL`
        ,Sum(ERAB_rel_user_inactivity) as 'ERAB_rel_user_inactivity'
        ,Sum(Radio_Connection_with_UE_lost) as 'Radio_Connection_with_UE_lost'
        ,Sum(ERAB_rel_UE_redirected) as 'ERAB_rel_UE_redirected'
        ,Sum(ERAB_rel_EUTRAN) as 'ERAB_rel_EUTRAN'
        ,Sum(ERAB_rel_GBR_congestion) as 'ERAB_rel_GBR_congestion'
        ,Sum(ERAB_rel_fail_Ho_Completion) as 'ERAB_rel_fail_Ho_Completion'
        ,Sum(ERAB_insuf_transport_resource) as 'ERAB_insuf_transport_resource'
        ,SUM(ERAB_rel_exp_HO_Guard_Time) AS 'ERAB_rel_exp_HO_Guard_Time'
        ,sum(Transp_Res_Unavailable) as 'Transp_Res_Unavailable'
        ,sum(Number_UEs_active_2_Scells) as 'Number_UEs_active_2_Scells'
        FROM isat_report.susy_4Gperfcell_2 a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "sitelevel":
        sqlscript_query ="""SELECT a.xDate,a.xHour,a.SITE_ID,a.Band
        ,round(100*(SUM(a.`Cell_Availability num`)/SUM(a.`Cell_Availability denum`)),2) AS `Cell_Availability`
        ,round(100*((SUM(a.`CSSR num1`)/SUM(a.`CSSR denum1`))*(SUM(a.`CSSR num2`)/SUM(a.`CSSR denum2`))*(SUM(a.`CSSR num3`)/SUM(a.`CSSR denum3`))),2) AS `CSSR`
        ,round(100*(SUM(a.`S1_Establisment_SR num`)/SUM(a.`S1_Establisment_SR denum`)),2) AS `S1_Establisment_SR`
        ,round(100*(SUM(a.`E-RAB_Drop num`)/SUM(a.`E-RAB_Drop denum`)),2) AS `E-RAB_Drop`
        ,round(100*(SUM(a.`Intra_HO num`)/SUM(a.`Intra_HO denum`)),2) AS `Intra_HO`
        ,round(100*(SUM(a.`Inter_Freq_HO num`)/SUM(a.`Inter_Freq_HO denum`)),2) AS `Inter_Freq_HO`
        ,ROUND(SUM(a.`Total_Payload(MBytes)`),2) AS `Total_Payload(MBytes)`
        ,round((SUM(a.`LTE_IP_User_Throughput_DL num`)/SUM(a.`LTE_IP_User_Throughput_DL denum`)),2) AS `LTE_IP_User_Throughput_DL`
        ,Sum(ERAB_rel_user_inactivity) as 'ERAB_rel_user_inactivity'
        ,Sum(Radio_Connection_with_UE_lost) as 'Radio_Connection_with_UE_lost'
        ,Sum(ERAB_rel_UE_redirected) as 'ERAB_rel_UE_redirected'
        ,Sum(ERAB_rel_EUTRAN) as 'ERAB_rel_EUTRAN'
        ,Sum(ERAB_rel_GBR_congestion) as 'ERAB_rel_GBR_congestion'
        ,Sum(ERAB_rel_fail_Ho_Completion) as 'ERAB_rel_fail_Ho_Completion'
        ,Sum(ERAB_insuf_transport_resource) as 'ERAB_insuf_transport_resource'
        ,SUM(ERAB_rel_exp_HO_Guard_Time) AS 'ERAB_rel_exp_HO_Guard_Time'
        ,sum(Transp_Res_Unavailable) as 'Transp_Res_Unavailable'
        ,sum(Number_UEs_active_2_Scells) as 'Number_UEs_active_2_Scells'
        ,round(sum(numRSSI)/sum(denumrssi),2) as RSSI_PUCCH
        FROM isat_report.susy_4Gperfcell_2 a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "agg":
        sqlscript_query ="""SELECT a.xDate,a.xHour,a.Band
        ,round(100*(SUM(a.`Cell_Availability num`)/SUM(a.`Cell_Availability denum`)),2) AS `Cell_Availability`
        ,round(100*((SUM(a.`CSSR num1`)/SUM(a.`CSSR denum1`))*(SUM(a.`CSSR num2`)/SUM(a.`CSSR denum2`))*(SUM(a.`CSSR num3`)/SUM(a.`CSSR denum3`))),2) AS `CSSR`
        ,round(100*(SUM(a.`S1_Establisment_SR num`)/SUM(a.`S1_Establisment_SR denum`)),2) AS `S1_Establisment_SR`
        ,round(100*(SUM(a.`E-RAB_Drop num`)/SUM(a.`E-RAB_Drop denum`)),2) AS `E-RAB_Drop`
        ,round(100*(SUM(a.`Intra_HO num`)/SUM(a.`Intra_HO denum`)),2) AS `Intra_HO`
        ,round(100*(SUM(a.`Inter_Freq_HO num`)/SUM(a.`Inter_Freq_HO denum`)),2) AS `Inter_Freq_HO`
        ,ROUND(SUM(a.`Total_Payload(MBytes)`),2) AS `Total_Payload(MBytes)`
        ,round((SUM(a.`LTE_IP_User_Throughput_DL num`)/SUM(a.`LTE_IP_User_Throughput_DL denum`)),2) AS `LTE_IP_User_Throughput_DL`
        ,Sum(ERAB_rel_user_inactivity) as 'ERAB_rel_user_inactivity'
        ,Sum(Radio_Connection_with_UE_lost) as 'Radio_Connection_with_UE_lost'
        ,Sum(ERAB_rel_UE_redirected) as 'ERAB_rel_UE_redirected'
        ,Sum(ERAB_rel_EUTRAN) as 'ERAB_rel_EUTRAN'
        ,Sum(ERAB_rel_GBR_congestion) as 'ERAB_rel_GBR_congestion'
        ,Sum(ERAB_rel_fail_Ho_Completion) as 'ERAB_rel_fail_Ho_Completion'
        ,Sum(ERAB_insuf_transport_resource) as 'ERAB_insuf_transport_resource'
        ,SUM(ERAB_rel_exp_HO_Guard_Time) AS 'ERAB_rel_exp_HO_Guard_Time'
        ,sum(Transp_Res_Unavailable) as 'Transp_Res_Unavailable'
        ,sum(Number_UEs_active_2_Scells) as 'Number_UEs_active_2_Scells'
        ,round(sum(numRSSI)/sum(denumrssi),2) as RSSI_PUCCH
        FROM isat_report.susy_4Gperfcell_2 a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "mrbtsidlevel":
        sqlscript_query ="""SELECT a.xDate,a.xHour,a.SITE_ID,a.Band,a.MRBTS_ID,a.LNCEL_ID
        ,round(100*(SUM(a.`Cell_Availability num`)/SUM(a.`Cell_Availability denum`)),2) AS `Cell_Availability`
        ,round(100*((SUM(a.`CSSR num1`)/SUM(a.`CSSR denum1`))*(SUM(a.`CSSR num2`)/SUM(a.`CSSR denum2`))*(SUM(a.`CSSR num3`)/SUM(a.`CSSR denum3`))),2) AS `CSSR`
        ,round(100*(SUM(a.`S1_Establisment_SR num`)/SUM(a.`S1_Establisment_SR denum`)),2) AS `S1_Establisment_SR`
        ,round(100*(SUM(a.`E-RAB_Drop num`)/SUM(a.`E-RAB_Drop denum`)),2) AS `E-RAB_Drop`
        ,round(100*(SUM(a.`Intra_HO num`)/SUM(a.`Intra_HO denum`)),2) AS `Intra_HO`
        ,round(100*(SUM(a.`Inter_Freq_HO num`)/SUM(a.`Inter_Freq_HO denum`)),2) AS `Inter_Freq_HO`
        ,ROUND(SUM(a.`Total_Payload(MBytes)`),2) AS `Total_Payload(MBytes)`
        ,round((SUM(a.`LTE_IP_User_Throughput_DL num`)/SUM(a.`LTE_IP_User_Throughput_DL denum`)),2) AS `LTE_IP_User_Throughput_DL`
        ,Sum(ERAB_rel_user_inactivity) as 'ERAB_rel_user_inactivity'
        ,Sum(Radio_Connection_with_UE_lost) as 'Radio_Connection_with_UE_lost'
        ,Sum(ERAB_rel_UE_redirected) as 'ERAB_rel_UE_redirected'
        ,Sum(ERAB_rel_EUTRAN) as 'ERAB_rel_EUTRAN'
        ,Sum(ERAB_rel_GBR_congestion) as 'ERAB_rel_GBR_congestion'
        ,Sum(ERAB_rel_fail_Ho_Completion) as 'ERAB_rel_fail_Ho_Completion'
        ,Sum(ERAB_insuf_transport_resource) as 'ERAB_insuf_transport_resource'
        ,SUM(ERAB_rel_exp_HO_Guard_Time) AS 'ERAB_rel_exp_HO_Guard_Time'
        ,sum(Transp_Res_Unavailable) as 'Transp_Res_Unavailable'
        ,sum(Number_UEs_active_2_Scells) as 'Number_UEs_active_2_Scells'
        ,round(sum(numRSSI)/sum(denumrssi),2) as RSSI_PUCCH
        FROM isat_report.susy_4Gperfcell_2 a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "plr_mrbts":
        sqlscript_query = """select
            xDate
            ,xHour
            ,MRBTS_ID
            ,MRBTSname
            ,TWAMP_ID
            ,AVGRTT
            ,MAXRTT
            ,MINRTT
            ,TXTWAMPMESSAGES
            ,LOSTTWAMPMESSAGES
            ,Max_AVGRTT
            ,Max_MAXRTT
            ,Max_MINRTT
            ,Max_TXTWAMPMESSAGES
            ,Max_LOSTTWAMPMESSAGES
            ,PLR
            from isat_report.susy_plr a

        """

    elif Request == "2G_MC_perf":
        sqlscript_query ="""SELECT a.xDate, a.xHour, a.REGION, a.MICRO_CLUSTER, a.BAND
        ,round(100*(sum(a.Cell_avail_num)/sum(a.tch_avail_Den)),2) as tch_avail
        ,round(100*(sum(a.TBF_DROP_NUM)/sum(a.TBF_DROP_DEN)),2) AS TBF_DROP
        ,round(100*(sum(a.CSSR_NUM)/sum(a.CSSR_DEN)),2) as CSSR
        ,round(sum(a.gsm_data_total_traffic_DL),2) as gsm_data_total_traffic_DL
        ,round(100*(sum(a.Drop_Call_Rate_2_NUM)/sum(a.Drop_Call_Rate_2_DEN)),2) as Drop_Call_Rate_2
        ,round(sum(a.TCH_Traffic_trf_24c),2) AS 'TCH_Traffic_trf_24c'
        ,ROUND(100*(sum(a.HOSR_NUM)/sum(a.HOSR_DEN)),2) AS 'HOSR'
        ,ROUND(100*(sum(a.TASR_NUM)/sum(a.TASR_DENUM)),2) AS 'TASR'
        ,ROUND(100*(sum(a.SDCCH_DROP_NUM)/sum(a.SDCCH_DROP_DENUM)),2) AS 'SDCCH_DROP'
        ,ROUND(100*(sum(a.DLQUAL0_5_NUM)/sum(a.DLQUAL0_5_DENUM)),2) AS 'DLQUAL0_5'
        ,ROUND(100*(sum(a.ULQUAL0_5_NUM)/sum(a.ULQUAL0_5_DENUM)),2) AS 'ULQUAL0_5'

        FROM isat_report.susy_2gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "2G_subMC_perf":
        sqlscript_query ="""SELECT a.xDate, a.xHour, a.REGION, a.Subscluster, a.BAND
        ,round(100*(sum(a.Cell_avail_num)/sum(a.tch_avail_Den)),2) as tch_avail
        ,round(100*(sum(a.TBF_DROP_NUM)/sum(a.TBF_DROP_DEN)),2) AS TBF_DROP
        ,round(100*(sum(a.CSSR_NUM)/sum(a.CSSR_DEN)),2) as CSSR
        ,round(sum(a.gsm_data_total_traffic_DL),2) as gsm_data_total_traffic_DL
        ,round(100*(sum(a.Drop_Call_Rate_2_NUM)/sum(a.Drop_Call_Rate_2_DEN)),2) as Drop_Call_Rate_2
        ,round(sum(a.TCH_Traffic_trf_24c),2) AS 'TCH_Traffic_trf_24c'
        ,ROUND(100*(sum(a.HOSR_NUM)/sum(a.HOSR_DEN)),2) AS 'HOSR'
        ,ROUND(100*(sum(a.TASR_NUM)/sum(a.TASR_DENUM)),2) AS 'TASR'
        ,ROUND(100*(sum(a.SDCCH_DROP_NUM)/sum(a.SDCCH_DROP_DENUM)),2) AS 'SDCCH_DROP'
        ,ROUND(100*(sum(a.DLQUAL0_5_NUM)/sum(a.DLQUAL0_5_DENUM)),2) AS 'DLQUAL0_5'
        ,ROUND(100*(sum(a.ULQUAL0_5_NUM)/sum(a.ULQUAL0_5_DENUM)),2) AS 'ULQUAL0_5'
        FROM isat_report.susy_2gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "2G_REGION":
        sqlscript_query ="""SELECT a.xDate,a.xHour,a.REGION,a.BAND
        ,round(100*(sum(a.Cell_avail_num)/sum(a.tch_avail_Den)),2) as tch_avail
        ,round(100*(sum(a.TBF_DROP_NUM)/sum(a.TBF_DROP_DEN)),2) AS TBF_DROP
        ,round(100*(sum(a.CSSR_NUM)/sum(a.CSSR_DEN)),2) as CSSR
        ,round(sum(a.gsm_data_total_traffic_DL),2) as gsm_data_total_traffic_DL
        ,round(100*(sum(a.Drop_Call_Rate_2_NUM)/sum(a.Drop_Call_Rate_2_DEN)),2) as Drop_Call_Rate_2
        ,round(sum(a.TCH_Traffic_trf_24c),2) AS 'TCH_Traffic_trf_24c'
        ,ROUND(100*(sum(a.HOSR_NUM)/sum(a.HOSR_DEN)),2) AS 'HOSR'
        ,ROUND(100*(sum(a.TASR_NUM)/sum(a.TASR_DENUM)),2) AS 'TASR'
        ,ROUND(100*(sum(a.SDCCH_DROP_NUM)/sum(a.SDCCH_DROP_DENUM)),2) AS 'SDCCH_DROP'
        ,ROUND(100*(sum(a.DLQUAL0_5_NUM)/sum(a.DLQUAL0_5_DENUM)),2) AS 'DLQUAL0_5'
        ,ROUND(100*(sum(a.ULQUAL0_5_NUM)/sum(a.ULQUAL0_5_DENUM)),2) AS 'ULQUAL0_5'
        FROM isat_report.susy_2gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "2G_CLUSTER2b":
        sqlscript_query ="""SELECT a.xDate, a.xHour, a.REGION, a.CLUSTER2b AS cluster, a.BAND
        ,round(100*(sum(a.Cell_avail_num)/sum(a.tch_avail_Den)),2) as tch_avail
        ,round(100*(sum(a.TBF_DROP_NUM)/sum(a.TBF_DROP_DEN)),2) AS TBF_DROP
        ,round(100*(sum(a.CSSR_NUM)/sum(a.CSSR_DEN)),2) as CSSR
        ,round(sum(a.gsm_data_total_traffic_DL),2) as gsm_data_total_traffic_DL
        ,round(100*(sum(a.Drop_Call_Rate_2_NUM)/sum(a.Drop_Call_Rate_2_DEN)),2) as Drop_Call_Rate_2
        ,round(sum(a.TCH_Traffic_trf_24c),2) AS 'TCH_Traffic_trf_24c'
        ,ROUND(100*(sum(a.HOSR_NUM)/sum(a.HOSR_DEN)),2) AS 'HOSR'
        ,ROUND(100*(sum(a.TASR_NUM)/sum(a.TASR_DENUM)),2) AS 'TASR'
        ,ROUND(100*(sum(a.SDCCH_DROP_NUM)/sum(a.SDCCH_DROP_DENUM)),2) AS 'SDCCH_DROP'
        ,ROUND(100*(sum(a.DLQUAL0_5_NUM)/sum(a.DLQUAL0_5_DENUM)),2) AS 'DLQUAL0_5'
        ,ROUND(100*(sum(a.ULQUAL0_5_NUM)/sum(a.ULQUAL0_5_DENUM)),2) AS 'ULQUAL0_5'
        FROM isat_report.susy_2gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "2G_BSClevel":
        sqlscript_query ="""SELECT a.xDate, a.xHour,a.BSC_ID
        ,round(100*(sum(a.Cell_avail_num)/sum(a.tch_avail_Den)),2) as tch_avail
        ,round(100*(sum(a.TBF_DROP_NUM)/sum(a.TBF_DROP_DEN)),2) AS TBF_DROP
        ,round(100*(sum(a.CSSR_NUM)/sum(a.CSSR_DEN)),2) as CSSR
        ,round(sum(a.gsm_data_total_traffic_DL),2) as gsm_data_total_traffic_DL
        ,round(100*(sum(a.Drop_Call_Rate_2_NUM)/sum(a.Drop_Call_Rate_2_DEN)),2) as Drop_Call_Rate_2
        ,round(sum(a.TCH_Traffic_trf_24c),2) AS 'TCH_Traffic_trf_24c'
        ,ROUND(100*(sum(a.HOSR_NUM)/sum(a.HOSR_DEN)),2) AS 'HOSR'
        ,ROUND(100*(sum(a.TASR_NUM)/sum(a.TASR_DENUM)),2) AS 'TASR'
        ,ROUND(100*(sum(a.SDCCH_DROP_NUM)/sum(a.SDCCH_DROP_DENUM)),2) AS 'SDCCH_DROP'
        ,ROUND(100*(sum(a.DLQUAL0_5_NUM)/sum(a.DLQUAL0_5_DENUM)),2) AS 'DLQUAL0_5'
        ,ROUND(100*(sum(a.ULQUAL0_5_NUM)/sum(a.ULQUAL0_5_DENUM)),2) AS 'ULQUAL0_5'
        FROM isat_report.susy_2gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "2G_sitelevel":
        sqlscript_query ="""SELECT a.xDate, a.xHour, a.REGION, a.site_id, a.BAND
        ,round(100*(sum(a.Cell_avail_num)/sum(a.tch_avail_Den)),2) as tch_avail
        ,round(100*(sum(a.TBF_DROP_NUM)/sum(a.TBF_DROP_DEN)),2) AS TBF_DROP
        ,round(100*(sum(a.CSSR_NUM)/sum(a.CSSR_DEN)),2) as CSSR
        ,round(sum(a.gsm_data_total_traffic_DL),2) as gsm_data_total_traffic_DL
        ,round(100*(sum(a.Drop_Call_Rate_2_NUM)/sum(a.Drop_Call_Rate_2_DEN)),2) as Drop_Call_Rate_2
        ,round(sum(a.TCH_Traffic_trf_24c),2) AS 'TCH_Traffic_trf_24c'
        ,ROUND(100*(sum(a.HOSR_NUM)/sum(a.HOSR_DEN)),2) AS 'HOSR'
        ,ROUND(100*(sum(a.TASR_NUM)/sum(a.TASR_DENUM)),2) AS 'TASR'
        ,ROUND(100*(sum(a.SDCCH_DROP_NUM)/sum(a.SDCCH_DROP_DENUM)),2) AS 'SDCCH_DROP'
        ,ROUND(100*(sum(a.DLQUAL0_5_NUM)/sum(a.DLQUAL0_5_DENUM)),2) AS 'DLQUAL0_5'
        ,ROUND(100*(sum(a.ULQUAL0_5_NUM)/sum(a.ULQUAL0_5_DENUM)),2) AS 'ULQUAL0_5'
        FROM isat_report.susy_2gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "2g_agg":
        sqlscript_query ="""SELECT a.xDate, a.xHour, a.REGION, a.BAND
        ,round(100*(sum(a.Cell_avail_num)/sum(a.tch_avail_Den)),2) as tch_avail
        ,round(100*(sum(a.TBF_DROP_NUM)/sum(a.TBF_DROP_DEN)),2) AS TBF_DROP
        ,round(100*(sum(a.CSSR_NUM)/sum(a.CSSR_DEN)),2) as CSSR
        ,round(sum(a.gsm_data_total_traffic_DL),2) as gsm_data_total_traffic_DL
        ,round(100*(sum(a.Drop_Call_Rate_2_NUM)/sum(a.Drop_Call_Rate_2_DEN)),2) as Drop_Call_Rate_2
        ,round(sum(a.TCH_Traffic_trf_24c),2) AS 'TCH_Traffic_trf_24c'
        ,ROUND(100*(sum(a.HOSR_NUM)/sum(a.HOSR_DEN)),2) AS 'HOSR'
        ,ROUND(100*(sum(a.TASR_NUM)/sum(a.TASR_DENUM)),2) AS 'TASR'
        ,ROUND(100*(sum(a.SDCCH_DROP_NUM)/sum(a.SDCCH_DROP_DENUM)),2) AS 'SDCCH_DROP'
        ,ROUND(100*(sum(a.DLQUAL0_5_NUM)/sum(a.DLQUAL0_5_DENUM)),2) AS 'DLQUAL0_5'
        ,ROUND(100*(sum(a.ULQUAL0_5_NUM)/sum(a.ULQUAL0_5_DENUM)),2) AS 'ULQUAL0_5'
        FROM isat_report.susy_2gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "2G_Cellidlevel":
        sqlscript_query ="""SELECT a.xDate, a.xHour, a.REGION, a.MICRO_CLUSTER, a.Subscluster, a.CLUSTER2b, a.site_id,a.BSC_ID, a.BCF_ID, a.BTS_ID, a.CELL_ID,a.BAND
        ,round(100*(sum(a.Cell_avail_num)/sum(a.tch_avail_Den)),2) as tch_avail
        ,round(100*(sum(a.TBF_DROP_NUM)/sum(a.TBF_DROP_DEN)),2) AS TBF_DROP
        ,round(100*(sum(a.CSSR_NUM)/sum(a.CSSR_DEN)),2) as CSSR
        ,round(sum(a.gsm_data_total_traffic_DL),2) as gsm_data_total_traffic_DL
        ,round(100*(sum(a.Drop_Call_Rate_2_NUM)/sum(a.Drop_Call_Rate_2_DEN)),2) as Drop_Call_Rate_2
        ,round(sum(a.TCH_Traffic_trf_24c),2) AS 'TCH_Traffic_trf_24c'
        ,ROUND(100*(sum(a.HOSR_NUM)/sum(a.HOSR_DEN)),2) AS 'HOSR'
        ,ROUND(100*(sum(a.TASR_NUM)/sum(a.TASR_DENUM)),2) AS 'TASR'
        ,ROUND(100*(sum(a.SDCCH_DROP_NUM)/sum(a.SDCCH_DROP_DENUM)),2) AS 'SDCCH_DROP'
        ,ROUND(100*(sum(a.DLQUAL0_5_NUM)/sum(a.DLQUAL0_5_DENUM)),2) AS 'DLQUAL0_5'
        ,ROUND(100*(sum(a.ULQUAL0_5_NUM)/sum(a.ULQUAL0_5_DENUM)),2) AS 'ULQUAL0_5'
        FROM isat_report.susy_2gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """

    elif Request == "3G_MC_perf":
        sqlscript_query ="""SELECT a.xdate, a.xHour, a.REGION, a.MICRO_CLUSTER, a.Band
        ,ROUND(100*(SUM(a.Cell_Avail_Num)/SUM(a.Cell_Avail_Denum)),2) AS 'Cell_Availability'
        ,ROUND(SUM(a.Traffic_CS),2) AS 'Traffic_CS'
        ,ROUND(SUM(a.Traffic_PS_Mbit),2) AS 'Traffic_PS_Mbit'
        ,ROUND(SUM(a.HSDPA_users_throughput_Num)/SUM(a.HSDPA_users_throughput_Denum),2) AS 'HSDPA_User_Thput'
        ,ROUND(100*((SUM(a.CSSR_CS_NUM_RRC)/SUM(a.CSSR_CS_DEN_RRC))*(SUM(a.CSSR_CS_NUM_RAB)/SUM(a.CSSR_CS_DEN_RAB))),2) AS 'CSSR_CS'
        ,ROUND(100*((SUM(a.CSSR_PS_NUM_RRC)/SUM(a.CSSR_PS_DEN_RRC))*(SUM(a.CSSR_PS_NUM_RAB)/SUM(a.CSSR_PS_DEN_RAB))),2) AS 'CSSR_PS'
        ,ROUND(100*(SUM(a.CDR_CS_NUM)/SUM(a.CDR_CS_DEN)),2) AS 'CDR_CS'
        ,ROUND(100*(SUM(a.CDR_PS_NUM)/SUM(a.CDR_PS_DEN)),2) AS 'CDR_PS'
        ,ROUND(100*(SUM(a.SHO_NUM)/SUM(a.SHO_DEN)),2) AS 'SHO'
        ,ROUND(100*(SUM(a.ISHO_NUM)/SUM(a.ISHO_DEN)),2) AS 'ISHO'
        ,ROUND(100*(SUM(a.IFHO_NUM)/SUM(a.IFHO_DEN)),2) AS 'IFHO'
        FROM isat_report.susy_3gperfcell a

        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "3G_subMC_perf":
        sqlscript_query ="""SELECT a.xdate, a.xHour, a.Subscluster, a.Band
        ,ROUND(100*(SUM(a.Cell_Avail_Num)/SUM(a.Cell_Avail_Denum)),2) AS 'Cell_Availability'
        ,ROUND(SUM(a.Traffic_CS),2) AS 'Traffic_CS'
        ,ROUND(SUM(a.Traffic_PS_Mbit),2) AS 'Traffic_PS_Mbit'
        ,ROUND(SUM(a.HSDPA_users_throughput_Num)/SUM(a.HSDPA_users_throughput_Denum),2) AS 'HSDPA_User_Thput'
        ,ROUND(100*((SUM(a.CSSR_CS_NUM_RRC)/SUM(a.CSSR_CS_DEN_RRC))*(SUM(a.CSSR_CS_NUM_RAB)/SUM(a.CSSR_CS_DEN_RAB))),2) AS 'CSSR_CS'
        ,ROUND(100*((SUM(a.CSSR_PS_NUM_RRC)/SUM(a.CSSR_PS_DEN_RRC))*(SUM(a.CSSR_PS_NUM_RAB)/SUM(a.CSSR_PS_DEN_RAB))),2) AS 'CSSR_PS'
        ,ROUND(100*(SUM(a.CDR_CS_NUM)/SUM(a.CDR_CS_DEN)),2) AS 'CDR_CS'
        ,ROUND(100*(SUM(a.CDR_PS_NUM)/SUM(a.CDR_PS_DEN)),2) AS 'CDR_PS'
        ,ROUND(100*(SUM(a.SHO_NUM)/SUM(a.SHO_DEN)),2) AS 'SHO'
        ,ROUND(100*(SUM(a.ISHO_NUM)/SUM(a.ISHO_DEN)),2) AS 'ISHO'
        ,ROUND(100*(SUM(a.IFHO_NUM)/SUM(a.IFHO_DEN)),2) AS 'IFHO'

        FROM isat_report.susy_3gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "3G_REGION":
        sqlscript_query ="""SELECT a.xdate, a.xHour, a.REGION, a.Band
        ,ROUND(100*(SUM(a.Cell_Avail_Num)/SUM(a.Cell_Avail_Denum)),2) AS 'Cell_Availability'
        ,ROUND(SUM(a.Traffic_CS),2) AS 'Traffic_CS'
        ,ROUND(SUM(a.Traffic_PS_Mbit),2) AS 'Traffic_PS_Mbit'
        ,ROUND(SUM(a.HSDPA_users_throughput_Num)/SUM(a.HSDPA_users_throughput_Denum),2) AS 'HSDPA_User_Thput'
        ,ROUND(100*((SUM(a.CSSR_CS_NUM_RRC)/SUM(a.CSSR_CS_DEN_RRC))*(SUM(a.CSSR_CS_NUM_RAB)/SUM(a.CSSR_CS_DEN_RAB))),2) AS 'CSSR_CS'
        ,ROUND(100*((SUM(a.CSSR_PS_NUM_RRC)/SUM(a.CSSR_PS_DEN_RRC))*(SUM(a.CSSR_PS_NUM_RAB)/SUM(a.CSSR_PS_DEN_RAB))),2) AS 'CSSR_PS'
        ,ROUND(100*(SUM(a.CDR_CS_NUM)/SUM(a.CDR_CS_DEN)),2) AS 'CDR_CS'
        ,ROUND(100*(SUM(a.CDR_PS_NUM)/SUM(a.CDR_PS_DEN)),2) AS 'CDR_PS'
        ,ROUND(100*(SUM(a.SHO_NUM)/SUM(a.SHO_DEN)),2) AS 'SHO'
        ,ROUND(100*(SUM(a.ISHO_NUM)/SUM(a.ISHO_DEN)),2) AS 'ISHO'
        ,ROUND(100*(SUM(a.IFHO_NUM)/SUM(a.IFHO_DEN)),2) AS 'IFHO'
        FROM isat_report.susy_3gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "3G_CLUSTER2b":
        sqlscript_query ="""SELECT a.xdate, a.xHour, a.CLUSTER2b as Cluster, a.Band
        ,ROUND(100*(SUM(a.Cell_Avail_Num)/SUM(a.Cell_Avail_Denum)),2) AS 'Cell_Availability'
        ,ROUND(SUM(a.Traffic_CS),2) AS 'Traffic_CS'
        ,ROUND(SUM(a.Traffic_PS_Mbit),2) AS 'Traffic_PS_Mbit'
        ,ROUND(SUM(a.HSDPA_users_throughput_Num)/SUM(a.HSDPA_users_throughput_Denum),2) AS 'HSDPA_User_Thput'
        ,ROUND(100*((SUM(a.CSSR_CS_NUM_RRC)/SUM(a.CSSR_CS_DEN_RRC))*(SUM(a.CSSR_CS_NUM_RAB)/SUM(a.CSSR_CS_DEN_RAB))),2) AS 'CSSR_CS'
        ,ROUND(100*((SUM(a.CSSR_PS_NUM_RRC)/SUM(a.CSSR_PS_DEN_RRC))*(SUM(a.CSSR_PS_NUM_RAB)/SUM(a.CSSR_PS_DEN_RAB))),2) AS 'CSSR_PS'
        ,ROUND(100*(SUM(a.CDR_CS_NUM)/SUM(a.CDR_CS_DEN)),2) AS 'CDR_CS'
        ,ROUND(100*(SUM(a.CDR_PS_NUM)/SUM(a.CDR_PS_DEN)),2) AS 'CDR_PS'
        ,ROUND(100*(SUM(a.SHO_NUM)/SUM(a.SHO_DEN)),2) AS 'SHO'
        ,ROUND(100*(SUM(a.ISHO_NUM)/SUM(a.ISHO_DEN)),2) AS 'ISHO'
        ,ROUND(100*(SUM(a.IFHO_NUM)/SUM(a.IFHO_DEN)),2) AS 'IFHO'
        FROM isat_report.susy_3gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "3G_RNC":
        sqlscript_query ="""SELECT a.xdate, a.xHour, a.RNC_ID
        ,ROUND(100*(SUM(a.Cell_Avail_Num)/SUM(a.Cell_Avail_Denum)),2) AS 'Cell_Availability'
        ,ROUND(SUM(a.Traffic_CS),2) AS 'Traffic_CS'
        ,ROUND(SUM(a.Traffic_PS_Mbit),2) AS 'Traffic_PS_Mbit'
        ,ROUND(SUM(a.HSDPA_users_throughput_Num)/SUM(a.HSDPA_users_throughput_Denum),2) AS 'HSDPA_User_Thput'
        ,ROUND(100*((SUM(a.CSSR_CS_NUM_RRC)/SUM(a.CSSR_CS_DEN_RRC))*(SUM(a.CSSR_CS_NUM_RAB)/SUM(a.CSSR_CS_DEN_RAB))),2) AS 'CSSR_CS'
        ,ROUND(100*((SUM(a.CSSR_PS_NUM_RRC)/SUM(a.CSSR_PS_DEN_RRC))*(SUM(a.CSSR_PS_NUM_RAB)/SUM(a.CSSR_PS_DEN_RAB))),2) AS 'CSSR_PS'
        ,ROUND(100*(SUM(a.CDR_CS_NUM)/SUM(a.CDR_CS_DEN)),2) AS 'CDR_CS'
        ,ROUND(100*(SUM(a.CDR_PS_NUM)/SUM(a.CDR_PS_DEN)),2) AS 'CDR_PS'
        ,ROUND(100*(SUM(a.SHO_NUM)/SUM(a.SHO_DEN)),2) AS 'SHO'
        ,ROUND(100*(SUM(a.ISHO_NUM)/SUM(a.ISHO_DEN)),2) AS 'ISHO'
        ,ROUND(100*(SUM(a.IFHO_NUM)/SUM(a.IFHO_DEN)),2) AS 'IFHO'
        FROM isat_report.susy_3gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "3G_sitelevel":
        sqlscript_query ="""SELECT a.xdate, a.xHour, a.REGION, a.SITE_ID, a.Band
        ,ROUND(100*(SUM(a.Cell_Avail_Num)/SUM(a.Cell_Avail_Denum)),2) AS 'Cell_Availability'
        ,ROUND(SUM(a.Traffic_CS),2) AS 'Traffic_CS'
        ,ROUND(SUM(a.Traffic_PS_Mbit),2) AS 'Traffic_PS_Mbit'
        ,ROUND(SUM(a.HSDPA_users_throughput_Num)/SUM(a.HSDPA_users_throughput_Denum),2) AS 'HSDPA_User_Thput'
        ,ROUND(100*((SUM(a.CSSR_CS_NUM_RRC)/SUM(a.CSSR_CS_DEN_RRC))*(SUM(a.CSSR_CS_NUM_RAB)/SUM(a.CSSR_CS_DEN_RAB))),2) AS 'CSSR_CS'
        ,ROUND(100*((SUM(a.CSSR_PS_NUM_RRC)/SUM(a.CSSR_PS_DEN_RRC))*(SUM(a.CSSR_PS_NUM_RAB)/SUM(a.CSSR_PS_DEN_RAB))),2) AS 'CSSR_PS'
        ,ROUND(100*(SUM(a.CDR_CS_NUM)/SUM(a.CDR_CS_DEN)),2) AS 'CDR_CS'
        ,ROUND(100*(SUM(a.CDR_PS_NUM)/SUM(a.CDR_PS_DEN)),2) AS 'CDR_PS'
        ,ROUND(100*(SUM(a.SHO_NUM)/SUM(a.SHO_DEN)),2) AS 'SHO'
        ,ROUND(100*(SUM(a.ISHO_NUM)/SUM(a.ISHO_DEN)),2) AS 'ISHO'
        ,ROUND(100*(SUM(a.IFHO_NUM)/SUM(a.IFHO_DEN)),2) AS 'IFHO'
        ,avg(RTWP) as RTWP
        FROM isat_report.susy_3gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "3g_agg":
        sqlscript_query ="""SELECT a.xdate, a.xHour, a.REGION, a.Band
        ,ROUND(100*(SUM(a.Cell_Avail_Num)/SUM(a.Cell_Avail_Denum)),2) AS 'Cell_Availability'
        ,ROUND(SUM(a.Traffic_CS),2) AS 'Traffic_CS'
        ,ROUND(SUM(a.Traffic_PS_Mbit),2) AS 'Traffic_PS_Mbit'
        ,ROUND(SUM(a.HSDPA_users_throughput_Num)/SUM(a.HSDPA_users_throughput_Denum),2) AS 'HSDPA_User_Thput'
        ,ROUND(100*((SUM(a.CSSR_CS_NUM_RRC)/SUM(a.CSSR_CS_DEN_RRC))*(SUM(a.CSSR_CS_NUM_RAB)/SUM(a.CSSR_CS_DEN_RAB))),2) AS 'CSSR_CS'
        ,ROUND(100*((SUM(a.CSSR_PS_NUM_RRC)/SUM(a.CSSR_PS_DEN_RRC))*(SUM(a.CSSR_PS_NUM_RAB)/SUM(a.CSSR_PS_DEN_RAB))),2) AS 'CSSR_PS'
        ,ROUND(100*(SUM(a.CDR_CS_NUM)/SUM(a.CDR_CS_DEN)),2) AS 'CDR_CS'
        ,ROUND(100*(SUM(a.CDR_PS_NUM)/SUM(a.CDR_PS_DEN)),2) AS 'CDR_PS'
        ,ROUND(100*(SUM(a.SHO_NUM)/SUM(a.SHO_DEN)),2) AS 'SHO'
        ,ROUND(100*(SUM(a.ISHO_NUM)/SUM(a.ISHO_DEN)),2) AS 'ISHO'
        ,ROUND(100*(SUM(a.IFHO_NUM)/SUM(a.IFHO_DEN)),2) AS 'IFHO'
        ,avg(RTWP) as RTWP
        FROM isat_report.susy_3gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    elif Request == "3G_celllevel":
        sqlscript_query="""
        SELECT a.xdate, a.xHour, a.REGION, a.WCEL_ID, a.SITE_ID
        ,ROUND(100*(SUM(a.Cell_Avail_Num)/SUM(a.Cell_Avail_Denum)),2) AS 'Cell_Availability'
        ,ROUND(SUM(a.Traffic_CS),2) AS 'Traffic_CS'
        ,ROUND(SUM(a.Traffic_PS_Mbit),2) AS 'Traffic_PS_Mbit'
        ,ROUND(SUM(a.HSDPA_users_throughput_Num)/SUM(a.HSDPA_users_throughput_Denum),2) AS 'HSDPA_User_Thput'
        ,ROUND(100*((SUM(a.CSSR_CS_NUM_RRC)/SUM(a.CSSR_CS_DEN_RRC))*(SUM(a.CSSR_CS_NUM_RAB)/SUM(a.CSSR_CS_DEN_RAB))),2) AS 'CSSR_CS'
        ,ROUND(100*((SUM(a.CSSR_PS_NUM_RRC)/SUM(a.CSSR_PS_DEN_RRC))*(SUM(a.CSSR_PS_NUM_RAB)/SUM(a.CSSR_PS_DEN_RAB))),2) AS 'CSSR_PS'
        ,ROUND(100*(SUM(a.CDR_CS_NUM)/SUM(a.CDR_CS_DEN)),2) AS 'CDR_CS'
        ,ROUND(100*(SUM(a.CDR_PS_NUM)/SUM(a.CDR_PS_DEN)),2) AS 'CDR_PS'
        ,ROUND(100*(SUM(a.SHO_NUM)/SUM(a.SHO_DEN)),2) AS 'SHO'
        ,ROUND(100*(SUM(a.ISHO_NUM)/SUM(a.ISHO_DEN)),2) AS 'ISHO'
        ,ROUND(100*(SUM(a.IFHO_NUM)/SUM(a.IFHO_DEN)),2) AS 'IFHO'
        ,avg(RTWP) as RTWP
        FROM isat_report.susy_3gperfcell a
        where xdate >='""" + aweekago.strftime("%Y-%m-%d") + """'
        """
    #===========================================
    elif Request == "2g_AOP_gplist":
        sqlscript_query = """Drop table if EXISTS isat_report.susy_2g_gp;
        CREATE TABLE isat_report.susy_2g_gp(
        	`bscid` INT(11) NOT NULL,
        	`bcfid` INT(11) NOT NULL,
        	`btsid` INT(11) NOT NULL,
        PRIMARY KEY (bscid,bcfid,btsid))
        SELECT b.bscid,b.bcfid,b.btsid FROM isat_report.susy_masterlist a JOIN isat_adm.t_list_2g_profile b ON a.SITE_ID = b.SITE_ID
        GROUP BY  b.bscid,b.bcfid,b.btsid;"""
    elif Request == "3g_AOP_gplist":
        sqlscript_query = """Drop table if EXISTS isat_report.susy_3g_gp;
        CREATE TABLE isat_report.susy_3g_gp(
        	`RNC_ID` INT(11) NOT NULL,
        	`WBTS_ID` INT(11) NOT NULL,
        	`CELL_ID` INT(11) NOT NULL,
        PRIMARY KEY (RNC_ID,WBTS_ID,CELL_ID))
        SELECT b.RNC_ID,b.WBTS_ID,b.CELL_ID FROM isat_report.susy_masterlist a JOIN isat_adm.t_list_3g_profile b ON a.SITE_ID = b.SITE_ID
        GROUP BY b.RNC_ID,b.WBTS_ID,b.CELL_ID;"""
    elif Request == "4g_AOP_gplist":
        sqlscript_query = """Drop table if EXISTS isat_report.susy_4g_gp;
        CREATE TABLE isat_report.susy_4g_gp(
        	`MRBTS_ID` INT(11) NOT NULL,
        	`LNCEL_ID` INT(11) NOT NULL,
        PRIMARY KEY (MRBTS_ID,LNCEL_ID))
        SELECT b.MRBTS_ID,b.LNCEL_ID FROM isat_report.susy_masterlist a JOIN isat_adm.t_list_4g_profile b ON a.SITE_ID = b.SITE_ID
        GROUP BY b.MRBTS_ID,b.LNCEL_ID;"""
    elif Request == "2g_all_gplist":
        sqlscript_query = """Drop table if EXISTS isat_report.susy_2g_gp;
        CREATE TABLE isat_report.susy_2g_gp(
        	`bscid` INT(11) NOT NULL,
        	`bcfid` INT(11) NOT NULL,
        	`btsid` INT(11) NOT NULL,
        PRIMARY KEY (bscid,bcfid,btsid))
        SELECT b.bscid,b.bcfid,b.btsid FROM isat_adm.t_list_2g_profile b
        GROUP BY  b.bscid,b.bcfid,b.btsid;"""
    elif Request == "3g_all_gplist":
        sqlscript_query = """Drop table if EXISTS isat_report.susy_3g_gp;
        CREATE TABLE isat_report.susy_3g_gp(
        	`RNC_ID` INT(11) NOT NULL,
        	`WBTS_ID` INT(11) NOT NULL,
        	`CELL_ID` INT(11) NOT NULL,
        PRIMARY KEY (RNC_ID,WBTS_ID,CELL_ID))
        SELECT b.RNC_ID,b.WBTS_ID,b.CELL_ID FROM isat_adm.t_list_3g_profile b
        GROUP BY b.RNC_ID,b.WBTS_ID,b.CELL_ID;"""
    elif Request == "4g_all_gplist":
        sqlscript_query = """Drop table if EXISTS isat_report.susy_4g_gp;
        CREATE TABLE isat_report.susy_4g_gp(
        	`MRBTS_ID` INT(11) NOT NULL,
        	`LNCEL_ID` INT(11) NOT NULL,
        PRIMARY KEY (MRBTS_ID,LNCEL_ID))
        SELECT b.MRBTS_ID,b.LNCEL_ID FROM isat_adm.t_list_4g_profile b
        GROUP BY b.MRBTS_ID,b.LNCEL_ID;"""
#==============================================================================================
    elif Request == "maintanan_weekly_counter4g":
        sqlscript_query = """
        CREATE TABLE isat_report.susy_4g_counter_hour_dummy (
        	`xDate` DATE NOT NULL,
        	`xHour` INT(11) NOT NULL,
        	`OBJ_ID` VARCHAR(80) NOT NULL,
        	`MRBTSname` VARCHAR(80) NULL DEFAULT NULL,
        	`LNBTSname` VARCHAR(80) NULL DEFAULT NULL,
        	`LNCELname` VARCHAR(80) NULL DEFAULT NULL,
        	`MRBTS_ID` INT(11) NOT NULL,
        	`LNBTS_ID` INT(11) NOT NULL,
        	`LNCEL_ID` INT(11) NOT NULL,
        	`PERIOD_DURATION` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_06_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_07_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_09_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_10_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_11_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_12_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_13_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_14_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_15_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_DL_CAT_16_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_UL_CAT_03_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_UL_CAT_05_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_UL_CAT_07_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_UL_CAT_08_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_UL_CAT_13_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_CAT_11_AVG` FLOAT NULL DEFAULT NULL,
        	`ACTIVE_UE_CAT_12_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_DL_CAP_UE_4CC_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_DL_3SCELLS_CONF_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_DL_3SCELLS_ACTIVE_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_DL_CAP_UE_2CC_MAX` FLOAT NULL DEFAULT NULL,
        	`CA_DL_CAP_UE_3CC_MAX` FLOAT NULL DEFAULT NULL,
        	`CA_SCELL_CONFIG_UE_MAX` FLOAT NULL DEFAULT NULL,
        	`CA_2SCELLS_CONF_UE_MAX` FLOAT NULL DEFAULT NULL,
        	`CA_SCELL_ACTIVE_UE_MAX` FLOAT NULL DEFAULT NULL,
        	`CA_2SCELLS_ACTIVE_UE_MAX` FLOAT NULL DEFAULT NULL,
        	`CA_3SCELLS_ACTIVE_UE_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_1_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_2_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_3_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_4_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_5_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_6_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_7_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_8_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_9_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_10_AVG` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_1_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_2_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_3_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_4_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_5_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_6_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_7_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_8_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_9_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_10_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_11_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_CAT_12_MAX` FLOAT NULL DEFAULT NULL,
        	`CA_UL_SCELL_CONFIG_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_UL_CAPAB_UE_2CC_AVG` FLOAT NULL DEFAULT NULL,
        	`RRC_CONNECTED_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`RRC_CONNECTED_UE_MAX` FLOAT NULL DEFAULT NULL,
        	`CELL_LOAD_ACTIVE_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`CELL_LOAD_ACTIVE_UE_MAX` FLOAT NULL DEFAULT NULL,
        	`ACT_UE_4LAYER_TM9_AVG` FLOAT NULL DEFAULT NULL,
        	`SUM_RRC_CONNECTED_UE` FLOAT NULL DEFAULT NULL,
        	`DENOM_RRC_CONNECTED_UE` FLOAT NULL DEFAULT NULL,
        	`SUM_ACT_UE` FLOAT NULL DEFAULT NULL,
        	`DENOM_ACT_UE` FLOAT NULL DEFAULT NULL,
        	`UE_INTER_FREQ_ANR_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_INTER_RAT_ANR_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_REL10_ACC_STRATUM_REL_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_REL11_ACC_STRATUM_REL_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_REL12_ACC_STRATUM_REL_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_REL8_ACC_STRATUM_REL_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_REL9_ACC_STRATUM_REL_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_UL_CA_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_UL_COMP_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_A_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_B_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_C_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_D_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_E_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_F_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_INTER_FREQ_ANR_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_INTER_RAT_ANR_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_REL10_ACC_STRATUM_REL_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_REL11_ACC_STRATUM_REL_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_REL12_ACC_STRATUM_REL_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_REL8_ACC_STRATUM_REL_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_REL9_ACC_STRATUM_REL_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_UL_CA_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_UL_COMP_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_A_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_B_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_C_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_D_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_E_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_CA_BANDWIDTH_CLASS_F_MAX` FLOAT NULL DEFAULT NULL,
        	`SUM_ACTIVE_UE_PW_CLASS1` FLOAT NULL DEFAULT NULL,
        	`DENOM_ACTIVE_UE_PW_CLASS1` FLOAT NULL DEFAULT NULL,
        	`UL_MU_MIMO_PAIR_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`UE_DRB_BUF_UL_DATA_QCI_1` FLOAT NULL DEFAULT NULL,
        	`UE_DRB_BUF_UL_DATA_NON_GBR` FLOAT NULL DEFAULT NULL,
        	`SUM_ACT_UE_DATA_UL` FLOAT NULL DEFAULT NULL,
        	`DENOM_ACT_UE_DATA_UL` FLOAT NULL DEFAULT NULL,
        	`SUM_ACT_UE_DATA_DL` FLOAT NULL DEFAULT NULL,
        	`DENOM_ACT_UE_DATA_DL` FLOAT NULL DEFAULT NULL,
        	`SUM_ACTIVE_UE_SCHED_DATA_UL` FLOAT NULL DEFAULT NULL,
        	`DENOM_ACTIVE_UE_SCHED_DATA_UL` FLOAT NULL DEFAULT NULL,
        	`SUM_ACTIVE_UE_SCHED_DATA_DL` FLOAT NULL DEFAULT NULL,
        	`DENOM_ACTIVE_UE_SCHED_DATA_DL` FLOAT NULL DEFAULT NULL,
        	`DL_UE_DATA_BUFFER_AVG` FLOAT NULL DEFAULT NULL,
        	`DL_UE_DATA_BUFFER_MAX` FLOAT NULL DEFAULT NULL,
        	`UL_UE_DATA_BUFFER_AVG` FLOAT NULL DEFAULT NULL,
        	`UL_UE_DATA_BUFFER_MAX` FLOAT NULL DEFAULT NULL,
        	`UE_DRB_BUF_DL_DATA_QCI_1` FLOAT NULL DEFAULT NULL,
        	`UE_DRB_BUF_DL_DATA_QCI_2` FLOAT NULL DEFAULT NULL,
        	`UE_DRB_BUF_DL_DATA_QCI_3` FLOAT NULL DEFAULT NULL,
        	`UE_DRB_BUF_DL_DATA_QCI_4` FLOAT NULL DEFAULT NULL,
        	`UE_DRB_BUF_DL_DATA_NON_GBR` FLOAT NULL DEFAULT NULL,
        	`CA_SCELL_ACT_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_2SCELLS_ACT_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_UL_SCELL_ACT_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`UL_INTRA_ENB_COMP_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`UL_INTR_ENB_COMP_L3_RRM_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_DL_CAP_UE_2CC_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_DL_CAPAB_UE_3CC_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_SCELL_CONFIG_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`CA_2SCELLS_CONFIG_UE_AVG` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_comp` FLOAT NULL DEFAULT NULL,
        	`sign_est_f_rrccompl_missing` FLOAT NULL DEFAULT NULL,
        	`sign_est_f_rrccompl_error` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_fail_rrmrac` FLOAT NULL DEFAULT NULL,
        	`epc_init_to_idle_ue_norm_rel` FLOAT NULL DEFAULT NULL,
        	`epc_init_to_idle_detach` FLOAT NULL DEFAULT NULL,
        	`epc_init_to_idle_rnl` FLOAT NULL DEFAULT NULL,
        	`epc_init_to_idle_other` FLOAT NULL DEFAULT NULL,
        	`enb_init_to_idle_norm_rel` FLOAT NULL DEFAULT NULL,
        	`enb_init_to_idle_rnl` FLOAT NULL DEFAULT NULL,
        	`enb_init_to_idle_other` FLOAT NULL DEFAULT NULL,
        	`period_duration_sum` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_att_mo_s` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_att_mt` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_att_mo_d` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_att_others` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_att_emg` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_comp_emg` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_fail_rb_emg` FLOAT NULL DEFAULT NULL,
        	`subframe_drx_active_ue` FLOAT NULL DEFAULT NULL,
        	`subframe_drx_sleep_ue` FLOAT NULL DEFAULT NULL,
        	`pre_empt_ue_context_non_gbr` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_rej_nemg` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_rej_emg` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_att_hiprio` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_succ_hiprio` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_rej_hiprio` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_att_del_tol` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_succ_mo_s` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_succ_mo_d` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_succ_mt` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_succ_del_tol` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_rej_mo_s` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_rej_mo_d` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_rej_mt` FLOAT NULL DEFAULT NULL,
        	`sign_conn_estab_rej_del_tol` FLOAT NULL DEFAULT NULL,
        	`s1_sign_conn_estab_att_ue` FLOAT NULL DEFAULT NULL,
        	`s1_sign_conn_estab_succ_ue` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_setup_att` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_setup_att_csfb` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_setup_succ` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_setup_succ_csfb` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_setup_fail_radio_int` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_mod_att` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_mod_att_csfb` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_mod_succ` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_mod_succ_csfb` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_rel_enb` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_rel_enb_user_ina` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_rel_enb_conn_loss` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_rel_enb_radio_int` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_rel_enb_eutran_reas` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_rel_enb_no_radio_res` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_rel_enb_rnl_unspec` FLOAT NULL DEFAULT NULL,
        	`ue_ctx_rel_enb_timer_ho` FLOAT NULL DEFAULT NULL,
        	`rej_rrc_conn_re_estab` FLOAT NULL DEFAULT NULL,
        	`disc_rrc_paging` FLOAT NULL DEFAULT NULL,
        	`rrc_paging_messages` FLOAT NULL DEFAULT NULL,
        	`rrc_paging_requests` FLOAT NULL DEFAULT NULL,
        	`rrc_con_re_estab_att` FLOAT NULL DEFAULT NULL,
        	`rrc_con_re_estab_succ` FLOAT NULL DEFAULT NULL,
        	`rrc_con_re_estab_att_ho_fail` FLOAT NULL DEFAULT NULL,
        	`rrc_con_re_estab_succ_ho_fail` FLOAT NULL DEFAULT NULL,
        	`rrc_con_re_estab_att_other` FLOAT NULL DEFAULT NULL,
        	`rrc_con_re_estab_succ_other` FLOAT NULL DEFAULT NULL,
        	`report_cgi_req` FLOAT NULL DEFAULT NULL,
        	`succ_cgi_reports` FLOAT NULL DEFAULT NULL,
        	`utran_report_cgi_att` FLOAT NULL DEFAULT NULL,
        	`utran_report_cgi_succ` FLOAT NULL DEFAULT NULL,
        	`rrc_con_rel_redir_h_enb` FLOAT NULL DEFAULT NULL,
        	`rrc_paging_etws_cmas` FLOAT NULL DEFAULT NULL,
        	`utran_report_cgi_incompl` FLOAT NULL DEFAULT NULL,
        	`rrc_con_stp_tim_mean` FLOAT NULL DEFAULT NULL,
        	`rrc_con_stp_tim_max` FLOAT NULL DEFAULT NULL,
        	`data_rb_stp_att` FLOAT NULL DEFAULT NULL,
        	`data_rb_stp_comp` FLOAT NULL DEFAULT NULL,
        	`data_rb_stp_fail` FLOAT NULL DEFAULT NULL,
        	`rb_rel_req_norm_rel` FLOAT NULL DEFAULT NULL,
        	`rb_rel_req_detach_proc` FLOAT NULL DEFAULT NULL,
        	`rb_rel_req_rnl` FLOAT NULL DEFAULT NULL,
        	`rb_rel_req_other` FLOAT NULL DEFAULT NULL,
        	`srb1_setup_att` FLOAT NULL DEFAULT NULL,
        	`srb1_setup_succ` FLOAT NULL DEFAULT NULL,
        	`srb1_setup_fail` FLOAT NULL DEFAULT NULL,
        	`srb2_setup_att` FLOAT NULL DEFAULT NULL,
        	`srb2_setup_succ` FLOAT NULL DEFAULT NULL,
        	`srb2_setup_fail` FLOAT NULL DEFAULT NULL,
        	`rb_rel_req_rnl_redir` FLOAT NULL DEFAULT NULL,
        	`erab_setup_time_mean` FLOAT NULL DEFAULT NULL,
        	`erab_setup_time_max` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_QCI_5` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_QCI_6` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_QCI_7` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_QCI_8` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_QCI_9` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_QCI_5` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_QCI_6` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_QCI_7` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_QCI_8` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_QCI_9` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DELAY_MEAN_QCI_1` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DELAY_MEAN_QCI_2` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DELAY_MEAN_QCI_3` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DELAY_MEAN_QCI_4` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DELAY_MEAN_QCI_5` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DELAY_MEAN_QCI_6` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DELAY_MEAN_QCI_7` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DELAY_MEAN_QCI_8` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DELAY_MEAN_QCI_9` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DL_QCI_5` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DL_QCI_6` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DL_QCI_7` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DL_QCI_8` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_DL_QCI_9` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_UL_QCI_5` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_UL_QCI_6` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_UL_QCI_7` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_UL_QCI_8` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_UL_QCI_9` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_FNA` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_QCI_1_FNA` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_QCI_2_FNA` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_QCI_3_FNA` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_UL_QCI_4_FNA` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_FNA` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_QCI_1_FNA` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_QCI_2_FNA` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_QCI_3_FNA` FLOAT NULL DEFAULT NULL,
        	`PDCP_SDU_LOSS_DL_QCI_4_FNA` FLOAT NULL DEFAULT NULL,
        	`HARQ_DURATION_QCI1_AVG` FLOAT NULL DEFAULT NULL,
        	`HARQ_DURATION_QCI2_AVG` FLOAT NULL DEFAULT NULL,
        	`HARQ_DURATION_QCI3_AVG` FLOAT NULL DEFAULT NULL,
        	`HARQ_DURATION_QCI4_AVG` FLOAT NULL DEFAULT NULL,
        	`HARQ_DURATION_QCI5_AVG` FLOAT NULL DEFAULT NULL,
        	`HARQ_DURATION_QCI6_AVG` FLOAT NULL DEFAULT NULL,
        	`HARQ_DURATION_QCI7_AVG` FLOAT NULL DEFAULT NULL,
        	`HARQ_DURATION_QCI8_AVG` FLOAT NULL DEFAULT NULL,
        	`HARQ_DURATION_QCI9_AVG` FLOAT NULL DEFAULT NULL,
        	`rssi_pucch_min` FLOAT NULL DEFAULT NULL,
        	`rssi_pucch_max` FLOAT NULL DEFAULT NULL,
        	`rssi_pucch_avg` FLOAT NULL DEFAULT NULL,
        	`rssi_pusch_min` FLOAT NULL DEFAULT NULL,
        	`rssi_pusch_max` FLOAT NULL DEFAULT NULL,
        	`rssi_pusch_avg` FLOAT NULL DEFAULT NULL,
        	`ul_bler_qpsk_all_trans_avg` FLOAT NULL DEFAULT NULL,
        	`ul_bler_16qam_all_trans_avg` FLOAT NULL DEFAULT NULL,
        	`ul_bler_qpsk_first_trans_avg` FLOAT NULL DEFAULT NULL,
        	`ul_bler_16qam_first_trans_avg` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level1` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level2` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level3` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level4` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level5` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level6` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level7` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level8` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level9` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level10` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level11` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level12` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level13` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level14` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level15` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level16` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level17` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level18` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level19` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level20` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level21` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level22` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level23` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level24` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level25` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level26` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level27` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level28` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level29` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level30` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level31` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_level32` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_min` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_max` FLOAT NULL DEFAULT NULL,
        	`ue_pwr_headroom_pusch_avg` FLOAT NULL DEFAULT NULL,
        	`sinr_pucch_min` FLOAT NULL DEFAULT NULL,
        	`sinr_pucch_max` FLOAT NULL DEFAULT NULL,
        	`sinr_pucch_avg` FLOAT NULL DEFAULT NULL,
        	`sinr_pusch_min` FLOAT NULL DEFAULT NULL,
        	`sinr_pusch_max` FLOAT NULL DEFAULT NULL,
        	`sinr_pusch_avg` FLOAT NULL DEFAULT NULL,
        	`ul_amc_upgrade` FLOAT NULL DEFAULT NULL,
        	`ul_amc_downgrade` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level1` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level2` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level3` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level4` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level5` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level6` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level7` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level8` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level9` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level10` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level11` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level12` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level13` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level14` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level15` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level16` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level17` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level18` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level19` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level20` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level21` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level22` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level23` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level24` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level25` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level26` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level27` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level28` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level29` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level30` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level31` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pusch_level32` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level1` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level2` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level3` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level4` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level5` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level6` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level7` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level8` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level9` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level10` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level11` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level12` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level13` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level14` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level15` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level16` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level17` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level18` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level19` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level20` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level21` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level22` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level23` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level24` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level25` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level26` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level27` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level28` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level29` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level30` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level31` FLOAT NULL DEFAULT NULL,
        	`ue_delta_tx_pucch_level32` FLOAT NULL DEFAULT NULL,
        	`rssi_cell_pucch_min` FLOAT NULL DEFAULT NULL,
        	`rssi_cell_pucch_max` FLOAT NULL DEFAULT NULL,
        	`rssi_cell_pucch_mean` FLOAT NULL DEFAULT NULL,
        	`rssi_cell_pusch_min` FLOAT NULL DEFAULT NULL,
        	`rssi_cell_pusch_max` FLOAT NULL DEFAULT NULL,
        	`rssi_cell_pusch_mean` FLOAT NULL DEFAULT NULL,
        	`sinr_cell_pucch_min` FLOAT NULL DEFAULT NULL,
        	`sinr_cell_pucch_max` FLOAT NULL DEFAULT NULL,
        	`sinr_cell_pucch_mean` FLOAT NULL DEFAULT NULL,
        	`sinr_cell_pusch_min` FLOAT NULL DEFAULT NULL,
        	`sinr_cell_pusch_max` FLOAT NULL DEFAULT NULL,
        	`sinr_cell_pusch_mean` FLOAT NULL DEFAULT NULL,
        	`avg_rtwp_rx_ant_1` FLOAT NULL DEFAULT NULL,
        	`avg_rtwp_rx_ant_2` FLOAT NULL DEFAULT NULL,
        	`avg_rtwp_rx_ant_3` FLOAT NULL DEFAULT NULL,
        	`avg_rtwp_rx_ant_4` FLOAT NULL DEFAULT NULL,
        	`avg_rtwp_rx_ant_5` FLOAT NULL DEFAULT NULL,
        	`avg_rtwp_rx_ant_6` FLOAT NULL DEFAULT NULL,
        	`avg_rtwp_rx_ant_7` FLOAT NULL DEFAULT NULL,
        	`avg_rtwp_rx_ant_8` FLOAT NULL DEFAULT NULL,
        	`max_rtwp` FLOAT NULL DEFAULT NULL,
        	`ul_iot_pusch_dist_bin_0` FLOAT NULL DEFAULT NULL,
        	`ul_iot_pusch_dist_bin_1` FLOAT NULL DEFAULT NULL,
        	`ul_iot_pusch_dist_bin_2` FLOAT NULL DEFAULT NULL,
        	`ul_iot_pusch_dist_bin_3` FLOAT NULL DEFAULT NULL,
        	`ul_iot_pusch_dist_bin_4` FLOAT NULL DEFAULT NULL,
        	`ul_iot_pusch_dist_bin_5` FLOAT NULL DEFAULT NULL,
        	`ul_iot_pusch_dist_bin_6` FLOAT NULL DEFAULT NULL,
        	`ul_iot_pusch_dist_bin_7` FLOAT NULL DEFAULT NULL,
        	`ul_iot_pusch_dist_bin_8` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_0` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_1` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_2` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_3` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_4` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_5` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_6` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_7` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_8` FLOAT NULL DEFAULT NULL,
        	`avg_sir_dist_bin_9` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_00` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_01` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_02` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_03` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_04` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_05` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_06` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_07` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_08` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_09` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_10` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_11` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_12` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_13` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_14` FLOAT NULL DEFAULT NULL,
        	`ue_rep_cqi_level_15` FLOAT NULL DEFAULT NULL,
        	`cqi_off_min` FLOAT NULL DEFAULT NULL,
        	`cqi_off_max` FLOAT NULL DEFAULT NULL,
        	`cqi_off_mean` FLOAT NULL DEFAULT NULL,
        	`mimo_ol_div` FLOAT NULL DEFAULT NULL,
        	`mimo_ol_sm` FLOAT NULL DEFAULT NULL,
        	`mimo_cl_1cw` FLOAT NULL DEFAULT NULL,
        	`mimo_cl_2cw` FLOAT NULL DEFAULT NULL,
        	`mimo_switch_ol` FLOAT NULL DEFAULT NULL,
        	`mimo_switch_cl` FLOAT NULL DEFAULT NULL,
        	`pdcch_alloc_pdsch_harq` FLOAT NULL DEFAULT NULL,
        	`pdcch_alloc_pdsch_harq_no_res` FLOAT NULL DEFAULT NULL,
        	`tm8_dual_bf_mode` FLOAT NULL DEFAULT NULL,
        	`tm8_single_bf_mode` FLOAT NULL DEFAULT NULL,
        	`tm8_txdiv_mode` FLOAT NULL DEFAULT NULL,
        	`tm8_dual_user_single_bf_mode` FLOAT NULL DEFAULT NULL,
        	`pdcch_power_avg` FLOAT NULL DEFAULT NULL,
        	`tm7_bf_mode` FLOAT NULL DEFAULT NULL,
        	`tm7_txdiv_mode` FLOAT NULL DEFAULT NULL,
        	`avg_trans_pwr` FLOAT NULL DEFAULT NULL,
        	`max_trans_pwr` FLOAT NULL DEFAULT NULL,
        	`intra_ho_prep_fail_nb` FLOAT NULL DEFAULT NULL,
        	`intra_ho_att_nb` FLOAT NULL DEFAULT NULL,
        	`intra_ho_succ_nb` FLOAT NULL DEFAULT NULL,
        	`intra_ho_drops_nb` FLOAT NULL DEFAULT NULL,
        	`inter_ho_prep_fail_ac_nb` FLOAT NULL DEFAULT NULL,
        	`inter_ho_att_nb` FLOAT NULL DEFAULT NULL,
        	`inter_ho_succ_nb` FLOAT NULL DEFAULT NULL,
        	`inter_ho_fail_nb` FLOAT NULL DEFAULT NULL,
        	`inter_ho_drops_nb` FLOAT NULL DEFAULT NULL,
        	`intra_ho_fail_nb` FLOAT NULL DEFAULT NULL,
        	`inter_ho_prep_fail_oth_nb` FLOAT NULL DEFAULT NULL,
        	`inter_ho_prep_fail_time_nb` FLOAT NULL DEFAULT NULL,
        	`mro_late_ho_nb` FLOAT NULL DEFAULT NULL,
        	`mro_early_type1_ho_nb` FLOAT NULL DEFAULT NULL,
        	`mro_early_type2_ho_nb` FLOAT NULL DEFAULT NULL,
        	`mro_ping_pong_ho_nb` FLOAT NULL DEFAULT NULL,
        	`csfb_redir_cr_att` FLOAT NULL DEFAULT NULL,
        	`csfb_redir_cr_cmode_att` FLOAT NULL DEFAULT NULL,
        	`csfb_redir_cr_emergency_att` FLOAT NULL DEFAULT NULL,
        	`isys_ho_prep` FLOAT NULL DEFAULT NULL,
        	`isys_ho_prep_fail_tim` FLOAT NULL DEFAULT NULL,
        	`isys_ho_prep_fail_ac` FLOAT NULL DEFAULT NULL,
        	`isys_ho_prep_fail_oth` FLOAT NULL DEFAULT NULL,
        	`isys_ho_att` FLOAT NULL DEFAULT NULL,
        	`isys_ho_succ` FLOAT NULL DEFAULT NULL,
        	`isys_ho_fail` FLOAT NULL DEFAULT NULL,
        	`nacc_to_gsm_att` FLOAT NULL DEFAULT NULL,
        	`nacc_to_gsm_succ` FLOAT NULL DEFAULT NULL,
        	`nacc_to_gsm_fail` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_srvcc_att` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_srvcc_succ` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_srvcc_fail` FLOAT NULL DEFAULT NULL,
        	`csfb_psho_utran_att` FLOAT NULL DEFAULT NULL,
        	`isys_ho_geran_srvcc_att` FLOAT NULL DEFAULT NULL,
        	`isys_ho_geran_srvcc_succ` FLOAT NULL DEFAULT NULL,
        	`isys_ho_geran_srvcc_fail` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_prep_fail_tim_nb` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_prep_fail_ac_nb` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_prep_fail_oth_nb` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_att_nb` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_succ_nb` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_fail_nb` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_prep_nb` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_srvcc_att_nb` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_srvcc_succ_nb` FLOAT NULL DEFAULT NULL,
        	`isys_ho_utran_srvcc_fail_nb` FLOAT NULL DEFAULT NULL,
        	`inter_enb_ho_prep` FLOAT NULL DEFAULT NULL,
        	`fail_enb_ho_prep_time` FLOAT NULL DEFAULT NULL,
        	`fail_enb_ho_prep_other` FLOAT NULL DEFAULT NULL,
        	`att_inter_enb_ho` FLOAT NULL DEFAULT NULL,
        	`succ_inter_enb_ho` FLOAT NULL DEFAULT NULL,
        	`fail_enb_ho_prep_ac` FLOAT NULL DEFAULT NULL,
        	`inter_enb_ho_fail` FLOAT NULL DEFAULT NULL,
        	`inter_enb_s1_ho_prep` FLOAT NULL DEFAULT NULL,
        	`inter_s1_ho_prep_fail_time` FLOAT NULL DEFAULT NULL,
        	`inter_s1_ho_prep_fail_norr` FLOAT NULL DEFAULT NULL,
        	`inter_s1_ho_prep_fail_other` FLOAT NULL DEFAULT NULL,
        	`inter_enb_s1_ho_att` FLOAT NULL DEFAULT NULL,
        	`inter_enb_s1_ho_succ` FLOAT NULL DEFAULT NULL,
        	`inter_enb_s1_ho_fail` FLOAT NULL DEFAULT NULL,
        	`tot_not_start_ho_prep` FLOAT NULL DEFAULT NULL,
        	`tot_ho_decision` FLOAT NULL DEFAULT NULL,
        	`intra_enb_ho_prep` FLOAT NULL DEFAULT NULL,
        	`fail_enb_ho_prep_oth` FLOAT NULL DEFAULT NULL,
        	`att_intra_enb_ho` FLOAT NULL DEFAULT NULL,
        	`succ_intra_enb_ho` FLOAT NULL DEFAULT NULL,
        	`enb_ho_drop_rlfail` FLOAT NULL DEFAULT NULL,
        	`enb_ho_drop_otherfail` FLOAT NULL DEFAULT NULL,
        	`enb_intra_ho_fail` FLOAT NULL DEFAULT NULL,
        	`ho_intfreq_att` FLOAT NULL DEFAULT NULL,
        	`ho_intfreq_gap_att` FLOAT NULL DEFAULT NULL,
        	`ho_intfreq_succ` FLOAT NULL DEFAULT NULL,
        	`ho_intfreq_gap_succ` FLOAT NULL DEFAULT NULL,
        	`ho_intfreq_fail` FLOAT NULL DEFAULT NULL,
        	`ho_intfreq_gap_fail` FLOAT NULL DEFAULT NULL,
        	`ho_emg_prep` FLOAT NULL DEFAULT NULL,
        	`ho_emg_prep_fail` FLOAT NULL DEFAULT NULL,
        	`ho_emg_att` FLOAT NULL DEFAULT NULL,
        	`ho_emg_succ` FLOAT NULL DEFAULT NULL,
        	`ho_drx_att` FLOAT NULL DEFAULT NULL,
        	`ho_drx_succ` FLOAT NULL DEFAULT NULL,
        	`mro_late_ho` FLOAT NULL DEFAULT NULL,
        	`mro_early_type1_ho` FLOAT NULL DEFAULT NULL,
        	`mro_early_type2_ho` FLOAT NULL DEFAULT NULL,
        	`ho_lb_att` FLOAT NULL DEFAULT NULL,
        	`ho_lb_succ` FLOAT NULL DEFAULT NULL,
        	`ho_sb_att` FLOAT NULL DEFAULT NULL,
        	`ho_sb_succ` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_att` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_att_tc` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_att_rr` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_att_rl` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_att_ro` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_succ` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_succ_tc` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_succ_rr` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_succ_rl` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_succ_ro` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_fail_rac` FLOAT NULL DEFAULT NULL,
        	`ho_prep_in_fail_tac` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_setup_attempts` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_setup_completions` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_setup_fail_rnl` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_setup_fail_trport` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_setup_fail_resour` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_setup_fail_oth` FLOAT NULL DEFAULT NULL,
        	`epc_eps_bearer_rel_req_norm` FLOAT NULL DEFAULT NULL,
        	`epc_eps_bearer_rel_req_detach` FLOAT NULL DEFAULT NULL,
        	`epc_eps_bearer_rel_req_rnl` FLOAT NULL DEFAULT NULL,
        	`epc_eps_bearer_rel_req_oth` FLOAT NULL DEFAULT NULL,
        	`enb_eps_bearer_rel_req_norm` FLOAT NULL DEFAULT NULL,
        	`enb_eps_bearer_rel_req_rnl` FLOAT NULL DEFAULT NULL,
        	`enb_eps_bearer_rel_req_oth` FLOAT NULL DEFAULT NULL,
        	`enb_eps_bearer_rel_req_tnl` FLOAT NULL DEFAULT NULL,
        	`enb_epsbear_rel_req_rnl_redir` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_setup_fail_ho` FLOAT NULL DEFAULT NULL,
        	`eps_bear_set_com_addit_qci1` FLOAT NULL DEFAULT NULL,
        	`epc_eps_bear_rel_req_n_qci1` FLOAT NULL DEFAULT NULL,
        	`epc_eps_bear_rel_req_d_qci1` FLOAT NULL DEFAULT NULL,
        	`epc_eps_bear_rel_req_r_qci1` FLOAT NULL DEFAULT NULL,
        	`epc_eps_bear_rel_req_o_qci1` FLOAT NULL DEFAULT NULL,
        	`enb_eps_bear_rel_req_n_qci1` FLOAT NULL DEFAULT NULL,
        	`enb_eps_bear_rel_req_o_qci1` FLOAT NULL DEFAULT NULL,
        	`enb_eps_bear_rel_req_t_qci1` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_att_ini_qci_1` FLOAT NULL DEFAULT NULL,
        	`eps_bear_stp_att_ini_non_gbr` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_att_add_qci_1` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_com_ini_qci1` FLOAT NULL DEFAULT NULL,
        	`eps_bear_stp_com_ini_non_gbr` FLOAT NULL DEFAULT NULL,
        	`enb_eps_bear_rel_req_r_qci1` FLOAT NULL DEFAULT NULL,
        	`enb_eps_bear_rel_req_rd_qci1` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_att_ini_qci_2` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_att_ini_qci_3` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_att_ini_qci_4` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_att_add_qci_2` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_att_add_qci_3` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_att_add_qci_4` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_com_ini_qci_2` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_com_ini_qci_3` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_com_ini_qci_4` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_com_add_qci_2` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_com_add_qci_3` FLOAT NULL DEFAULT NULL,
        	`eps_bearer_stp_com_add_qci_4` FLOAT NULL DEFAULT NULL,
        	`pre_empt_gbr_bearer` FLOAT NULL DEFAULT NULL,
        	`pre_empt_non_gbr_bearer` FLOAT NULL DEFAULT NULL,
        	`erab_rel_enb_act_qci1` FLOAT NULL DEFAULT NULL,
        	`erab_rel_enb_act_qci2` FLOAT NULL DEFAULT NULL,
        	`erab_rel_enb_act_qci3` FLOAT NULL DEFAULT NULL,
        	`erab_rel_enb_act_qci4` FLOAT NULL DEFAULT NULL,
        	`erab_rel_enb_act_non_gbr` FLOAT NULL DEFAULT NULL,
        	`erab_in_session_time_qci1` FLOAT NULL DEFAULT NULL,
        	`erab_in_session_time_qci2` FLOAT NULL DEFAULT NULL,
        	`erab_in_session_time_qci3` FLOAT NULL DEFAULT NULL,
        	`erab_in_session_time_qci4` FLOAT NULL DEFAULT NULL,
        	`erab_in_session_time_non_gbr` FLOAT NULL DEFAULT NULL,
        	`sum_simul_erab_qci_1` FLOAT NULL DEFAULT NULL,
        	`sum_simul_erab_qci_2` FLOAT NULL DEFAULT NULL,
        	`sum_simul_erab_qci_3` FLOAT NULL DEFAULT NULL,
        	`sum_simul_erab_qci_4` FLOAT NULL DEFAULT NULL,
        	`sum_simul_erab_qci_5` FLOAT NULL DEFAULT NULL,
        	`sum_simul_erab_qci_6` FLOAT NULL DEFAULT NULL,
        	`sum_simul_erab_qci_7` FLOAT NULL DEFAULT NULL,
        	`sum_simul_erab_qci_8` FLOAT NULL DEFAULT NULL,
        	`sum_simul_erab_qci_9` FLOAT NULL DEFAULT NULL,
        	`denom_sum_simul_erab` FLOAT NULL DEFAULT NULL,
        	`erab_setup_att_hiprio` FLOAT NULL DEFAULT NULL,
        	`erab_setup_succ_hiprio` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_att_qci1` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_att_qci2` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_att_qci3` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_att_qci4` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_att_qci5` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_att_qci6` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_att_qci7` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_att_qci8` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_att_qci9` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_att_qci1` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_att_qci2` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_att_qci3` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_att_qci4` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_att_qci5` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_att_qci6` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_att_qci7` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_att_qci8` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_att_qci9` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_succ_qci1` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_succ_qci2` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_succ_qci3` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_succ_qci4` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_succ_qci5` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_succ_qci6` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_succ_qci7` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_succ_qci8` FLOAT NULL DEFAULT NULL,
        	`erab_ini_setup_succ_qci9` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_succ_qci1` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_succ_qci2` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_succ_qci3` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_succ_qci4` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_succ_qci5` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_succ_qci6` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_succ_qci7` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_succ_qci8` FLOAT NULL DEFAULT NULL,
        	`erab_add_setup_succ_qci9` FLOAT NULL DEFAULT NULL,
        	`simul_erab_qci1_max` FLOAT NULL DEFAULT NULL,
        	`simul_erab_qci2_max` FLOAT NULL DEFAULT NULL,
        	`simul_erab_qci3_max` FLOAT NULL DEFAULT NULL,
        	`simul_erab_qci4_max` FLOAT NULL DEFAULT NULL,
        	`simul_erab_qci5_max` FLOAT NULL DEFAULT NULL,
        	`simul_erab_qci6_max` FLOAT NULL DEFAULT NULL,
        	`simul_erab_qci7_max` FLOAT NULL DEFAULT NULL,
        	`simul_erab_qci8_max` FLOAT NULL DEFAULT NULL,
        	`simul_erab_qci9_max` FLOAT NULL DEFAULT NULL,
        	`erab_nbr_dl_avg` FLOAT NULL DEFAULT NULL,
        	`erab_nbr_ul_avg` FLOAT NULL DEFAULT NULL,
        	`erab_nbr_dl_fail_ovl_avg` FLOAT NULL DEFAULT NULL,
        	`erab_nbr_ul_fail_ovl_avg` FLOAT NULL DEFAULT NULL,
        	`erab_mod_att_qci1` FLOAT NULL DEFAULT NULL,
        	`erab_mod_att_qci2` FLOAT NULL DEFAULT NULL,
        	`erab_mod_att_qci3` FLOAT NULL DEFAULT NULL,
        	`erab_mod_att_qci4` FLOAT NULL DEFAULT NULL,
        	`erab_mod_att_qci5` FLOAT NULL DEFAULT NULL,
        	`erab_mod_att_qci6` FLOAT NULL DEFAULT NULL,
        	`erab_mod_att_qci7` FLOAT NULL DEFAULT NULL,
        	`erab_mod_att_qci8` FLOAT NULL DEFAULT NULL,
        	`erab_mod_att_qci9` FLOAT NULL DEFAULT NULL,
        	`erab_mod_succ_qci1` FLOAT NULL DEFAULT NULL,
        	`erab_mod_succ_qci2` FLOAT NULL DEFAULT NULL,
        	`erab_mod_succ_qci3` FLOAT NULL DEFAULT NULL,
        	`erab_mod_succ_qci4` FLOAT NULL DEFAULT NULL,
        	`erab_mod_succ_qci5` FLOAT NULL DEFAULT NULL,
        	`erab_mod_succ_qci6` FLOAT NULL DEFAULT NULL,
        	`erab_mod_succ_qci7` FLOAT NULL DEFAULT NULL,
        	`erab_mod_succ_qci8` FLOAT NULL DEFAULT NULL,
        	`erab_mod_succ_qci9` FLOAT NULL DEFAULT NULL,
        	`erab_mod_fail_timer` FLOAT NULL DEFAULT NULL,
        	`erab_mod_fail_qci_nsupp` FLOAT NULL DEFAULT NULL,
        	`erab_mod_fail_rnl_unspec` FLOAT NULL DEFAULT NULL,
        	`ERAB_MOD_FAIL_RNL_RR_NA` FLOAT NULL DEFAULT NULL,
        	`ERAB_MOD_FAIL_TNL_TRU` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_ACT_QCI5` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_ACT_QCI6` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_ACT_QCI7` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_ACT_QCI8` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_ACT_QCI9` FLOAT NULL DEFAULT NULL,
        	`ERAB_INI_SETUP_FAIL_RNL_RRNA` FLOAT NULL DEFAULT NULL,
        	`ERAB_INI_SETUP_FAIL_TNL_TRU` FLOAT NULL DEFAULT NULL,
        	`ERAB_INI_SETUP_FAIL_RNL_UEL` FLOAT NULL DEFAULT NULL,
        	`ERAB_INI_SETUP_FAIL_RNL_RIP` FLOAT NULL DEFAULT NULL,
        	`ERAB_ADD_SETUP_FAIL_RNL_RRNA` FLOAT NULL DEFAULT NULL,
        	`ERAB_ADD_SETUP_FAIL_TNL_TRU` FLOAT NULL DEFAULT NULL,
        	`ERAB_ADD_SETUP_FAIL_RNL_UEL` FLOAT NULL DEFAULT NULL,
        	`ERAB_ADD_SETUP_FAIL_RNL_RIP` FLOAT NULL DEFAULT NULL,
        	`ERAB_ADD_SETUP_FAIL_UP` FLOAT NULL DEFAULT NULL,
        	`ERAB_ADD_SETUP_FAIL_RNL_MOB` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_INA` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_UEL` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_TNL_TRU` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_RED` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_EUGR` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_RRNA` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_PART` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_ATT` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_SUCC` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_FAIL_TIM` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_FAIL` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_INA_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_UEL_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_TNL_TRU_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_RED_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_EUGR_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_RRNA_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_PART_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_ATT_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_SUCC_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_FAIL_TIM_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_EPC_PATH_SWITCH` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_EPC_PATH_SWITCH_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_TNL_UNSP` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_TNL_UNSP_QCI1` FLOAT NULL DEFAULT NULL,
        	`SUCC_PART_AC_CHECK` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_EPC_PATH_SWITCH_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_TNL_UNSP_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_INA_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_UEL_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_TNL_TRU_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_RED_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_EUGR_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_ENB_RNL_RRNA_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_PART_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_ATT_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_SUCC_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_HO_FAIL_TIM_QCI2` FLOAT NULL DEFAULT NULL,
        	`EPC_EPS_BEAR_REL_REQ_R_QCI2` FLOAT NULL DEFAULT NULL,
        	`EPC_EPS_BEAR_REL_REQ_O_QCI2` FLOAT NULL DEFAULT NULL,
        	`EPC_EPS_BEAR_REL_REQ_N_QCI2` FLOAT NULL DEFAULT NULL,
        	`EPC_EPS_BEAR_REL_REQ_D_QCI2` FLOAT NULL DEFAULT NULL,
        	`ERAB_SUCC_RAC_TEMP_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_SUCC_TAC_TEMP_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_REL_TEMP_QCI1` FLOAT NULL DEFAULT NULL,
        	`ERAB_INI_SETUP_FAIL_NO_UE_LIC` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_vol_dl_dcch` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_vol_ul_dcch` FLOAT NULL DEFAULT NULL,
        	`rlc_pdu_vol_received` FLOAT NULL DEFAULT NULL,
        	`rlc_pdu_vol_transmitted` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_vol_ul` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_vol_dl` FLOAT NULL DEFAULT NULL,
        	`pdcp_data_rate_min_ul` FLOAT NULL DEFAULT NULL,
        	`pdcp_data_rate_max_ul` FLOAT NULL DEFAULT NULL,
        	`pdcp_data_rate_mean_ul` FLOAT NULL DEFAULT NULL,
        	`pdcp_data_rate_min_dl` FLOAT NULL DEFAULT NULL,
        	`pdcp_data_rate_max_dl` FLOAT NULL DEFAULT NULL,
        	`pdcp_data_rate_mean_dl` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs0` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs1` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs2` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs3` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs4` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs5` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs6` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs7` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs8` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs9` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs10` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs11` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs12` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs13` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs14` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs15` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs16` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs17` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs18` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs19` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs20` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs0` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs1` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs2` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs3` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs4` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs5` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs6` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs7` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs8` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs9` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs10` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs11` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs12` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs13` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs14` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs15` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs16` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs17` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs18` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs19` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs20` FLOAT NULL DEFAULT NULL,
        	`mac_sdu_vol_ul_ccch` FLOAT NULL DEFAULT NULL,
        	`mac_sdu_vol_ul_dcch` FLOAT NULL DEFAULT NULL,
        	`mac_sdu_vol_ul_dtch` FLOAT NULL DEFAULT NULL,
        	`mac_sdu_vol_bcch` FLOAT NULL DEFAULT NULL,
        	`mac_sdu_vol_pcch` FLOAT NULL DEFAULT NULL,
        	`mac_sdu_vol_dl_ccch` FLOAT NULL DEFAULT NULL,
        	`mac_sdu_vol_dl_dcch` FLOAT NULL DEFAULT NULL,
        	`mac_sdu_vol_dl_dtch` FLOAT NULL DEFAULT NULL,
        	`rrc_ul_vol` FLOAT NULL DEFAULT NULL,
        	`rrc_dl_vol` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_vol_ul_dtch` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_vol_dl_dtch` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs21` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs22` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs23` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs24` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs25` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs26` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs27` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs28` FLOAT NULL DEFAULT NULL,
        	`vol_orig_trans_dl_sch_tb` FLOAT NULL DEFAULT NULL,
        	`vol_re_rec_ul_sch_tb` FLOAT NULL DEFAULT NULL,
        	`vol_re_trans_dl_sch_tb` FLOAT NULL DEFAULT NULL,
        	`vol_orig_rec_ul_sch_tb` FLOAT NULL DEFAULT NULL,
        	`pdcp_data_rate_mean_ul_qci_1` FLOAT NULL DEFAULT NULL,
        	`pdcp_data_rate_mean_dl_qci_1` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs21` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs22` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs23` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs24` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs29` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs30` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pdsch_mcs31` FLOAT NULL DEFAULT NULL,
        	`rlc_pdu_dl_vol_ca_scell` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs25` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs26` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs27` FLOAT NULL DEFAULT NULL,
        	`tb_vol_pusch_mcs28` FLOAT NULL DEFAULT NULL,
        	`active_tti_ul` FLOAT NULL DEFAULT NULL,
        	`active_tti_dl` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_ul_qci_1` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_ul_qci_1` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_ul_qci_2` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_ul_qci_2` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_ul_qci_3` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_ul_qci_3` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_ul_qci_4` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_ul_qci_4` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_ul_qci_5` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_ul_qci_5` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_ul_qci_6` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_ul_qci_6` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_ul_qci_7` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_ul_qci_7` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_ul_qci_8` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_ul_qci_8` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_ul_qci_9` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_ul_qci_9` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_dl_qci_1` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_dl_qci_1` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_dl_qci_2` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_dl_qci_2` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_dl_qci_3` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_dl_qci_3` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_dl_qci_4` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_dl_qci_4` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_dl_qci_5` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_dl_qci_5` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_dl_qci_6` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_dl_qci_6` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_dl_qci_7` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_dl_qci_7` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_dl_qci_8` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_dl_qci_8` FLOAT NULL DEFAULT NULL,
        	`ip_tput_vol_dl_qci_9` FLOAT NULL DEFAULT NULL,
        	`ip_tput_time_dl_qci_9` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_ul_qci1` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_ul_qci2` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_ul_qci3` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_ul_qci4` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_ul_qci5` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_ul_qci6` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_ul_qci7` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_ul_qci8` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_ul_qci9` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_dl_qci1` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_dl_qci2` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_dl_qci3` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_dl_qci4` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_dl_qci5` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_dl_qci6` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_dl_qci7` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_dl_qci8` FLOAT NULL DEFAULT NULL,
        	`ip_tput_net_time_dl_qci9` FLOAT NULL DEFAULT NULL,
        	`min_avail_ul_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`max_avail_ul_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`mean_avail_ul_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`min_avail_dl_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`max_avail_dl_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`mean_avail_dl_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`min_alloc_ul_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`max_alloc_ul_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`mean_alloc_ul_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`min_alloc_dl_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`max_alloc_dl_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`mean_alloc_dl_prb_tti_ue` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_1` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_2` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_3` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_4` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_5` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_6` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_7` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_8` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_9` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_level_10` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_min` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_max` FLOAT NULL DEFAULT NULL,
        	`ul_prb_util_tti_mean` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_1` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_2` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_3` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_4` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_5` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_6` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_7` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_8` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_9` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_level_10` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_min` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_max` FLOAT NULL DEFAULT NULL,
        	`dl_prb_util_tti_mean` FLOAT NULL DEFAULT NULL,
        	`cce_avail_act_tti` FLOAT NULL DEFAULT NULL,
        	`agg1_used_pdcch` FLOAT NULL DEFAULT NULL,
        	`agg2_used_pdcch` FLOAT NULL DEFAULT NULL,
        	`agg4_used_pdcch` FLOAT NULL DEFAULT NULL,
        	`agg8_used_pdcch` FLOAT NULL DEFAULT NULL,
        	`agg1_blocked_pdcch` FLOAT NULL DEFAULT NULL,
        	`agg2_blocked_pdcch` FLOAT NULL DEFAULT NULL,
        	`agg4_blocked_pdcch` FLOAT NULL DEFAULT NULL,
        	`agg8_blocked_pdcch` FLOAT NULL DEFAULT NULL,
        	`prb_used_ul_total` FLOAT NULL DEFAULT NULL,
        	`prb_used_prach` FLOAT NULL DEFAULT NULL,
        	`prb_used_pucch` FLOAT NULL DEFAULT NULL,
        	`prb_used_pusch` FLOAT NULL DEFAULT NULL,
        	`prb_used_dl_total` FLOAT NULL DEFAULT NULL,
        	`prb_used_pbch` FLOAT NULL DEFAULT NULL,
        	`prb_used_pdcch` FLOAT NULL DEFAULT NULL,
        	`prb_used_pdsch` FLOAT NULL DEFAULT NULL,
        	`ue_per_ul_tti_avg` FLOAT NULL DEFAULT NULL,
        	`ue_per_ul_tti_max` FLOAT NULL DEFAULT NULL,
        	`ue_per_dl_tti_avg` FLOAT NULL DEFAULT NULL,
        	`ue_per_dl_tti_max` FLOAT NULL DEFAULT NULL,
        	`pdcch_1_ofdm_symbol` FLOAT NULL DEFAULT NULL,
        	`pdcch_2_ofdm_symbols` FLOAT NULL DEFAULT NULL,
        	`pdcch_3_ofdm_symbols` FLOAT NULL DEFAULT NULL,
        	`tti_bundling_mode_ue_avg` FLOAT NULL DEFAULT NULL,
        	`tti_bundling_grants` FLOAT NULL DEFAULT NULL,
        	`tti_bundl_retention_short` FLOAT NULL DEFAULT NULL,
        	`tti_bundl_retention_medium` FLOAT NULL DEFAULT NULL,
        	`tti_bundl_retention_long` FLOAT NULL DEFAULT NULL,
        	`ca_scell_config_att` FLOAT NULL DEFAULT NULL,
        	`ca_scell_config_succ` FLOAT NULL DEFAULT NULL,
        	`high_cell_load_lb` FLOAT NULL DEFAULT NULL,
        	`crg_used_tti_ul_grp_1` FLOAT NULL DEFAULT NULL,
        	`crg_used_tti_ul_grp_2` FLOAT NULL DEFAULT NULL,
        	`crg_used_tti_ul_grp_3` FLOAT NULL DEFAULT NULL,
        	`crg_used_tti_ul_grp_4` FLOAT NULL DEFAULT NULL,
        	`tti_pusch_available` FLOAT NULL DEFAULT NULL,
        	`crg_used_tti_dl_grp_1` FLOAT NULL DEFAULT NULL,
        	`crg_used_tti_dl_grp_2` FLOAT NULL DEFAULT NULL,
        	`crg_used_tti_dl_grp_3` FLOAT NULL DEFAULT NULL,
        	`crg_used_tti_dl_grp_4` FLOAT NULL DEFAULT NULL,
        	`tti_pdsch_available` FLOAT NULL DEFAULT NULL,
        	`ul_mu_mimo_sha_pusch_prb_avg` FLOAT NULL DEFAULT NULL,
        	`dl_cac_equal_zero` FLOAT NULL DEFAULT NULL,
        	`dl_cac_above_0_below_eq_20` FLOAT NULL DEFAULT NULL,
        	`dl_cac_above_20_below_eq_40` FLOAT NULL DEFAULT NULL,
        	`dl_cac_above_40_below_eq_60` FLOAT NULL DEFAULT NULL,
        	`dl_cac_above_60_below_eq_80` FLOAT NULL DEFAULT NULL,
        	`dl_cac_above_80_below_eq_100` FLOAT NULL DEFAULT NULL,
        	`dl_interfer_shap_use` FLOAT NULL DEFAULT NULL,
        	`dl_interfer_shap_amount` FLOAT NULL DEFAULT NULL,
        	`dl_interfer_shap_change` FLOAT NULL DEFAULT NULL,
        	`dl_ac_pdcch_eq_zero` FLOAT NULL DEFAULT NULL,
        	`dl_ac_pdcch_0_to_20` FLOAT NULL DEFAULT NULL,
        	`dl_ac_pdcch_20_to_40` FLOAT NULL DEFAULT NULL,
        	`dl_ac_pdcch_40_to_60` FLOAT NULL DEFAULT NULL,
        	`dl_ac_pdcch_60_to_80` FLOAT NULL DEFAULT NULL,
        	`dl_ac_pdcch_80_to_100` FLOAT NULL DEFAULT NULL,
        	`dl_ac_gbr_eq_zero` FLOAT NULL DEFAULT NULL,
        	`dl_ac_gbr_0_to_20` FLOAT NULL DEFAULT NULL,
        	`dl_ac_gbr_20_to_40` FLOAT NULL DEFAULT NULL,
        	`dl_ac_gbr_40_to_60` FLOAT NULL DEFAULT NULL,
        	`dl_ac_gbr_60_to_80` FLOAT NULL DEFAULT NULL,
        	`dl_ac_gbr_80_to_100` FLOAT NULL DEFAULT NULL,
        	`dl_ac_non_gbr_eq_zero` FLOAT NULL DEFAULT NULL,
        	`dl_ac_non_gbr_0_to_20` FLOAT NULL DEFAULT NULL,
        	`dl_ac_non_gbr_20_to_40` FLOAT NULL DEFAULT NULL,
        	`dl_ac_non_gbr_40_to_60` FLOAT NULL DEFAULT NULL,
        	`dl_ac_non_gbr_60_to_80` FLOAT NULL DEFAULT NULL,
        	`dl_ac_non_gbr_80_to_100` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_delay_dl_dtch_min` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_delay_dl_dtch_max` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_delay_dl_dtch_mean` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_delay_ul_dtch_min` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_delay_ul_dtch_max` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_delay_ul_dtch_mean` FLOAT NULL DEFAULT NULL,
        	`rach_stp_att_small_msg` FLOAT NULL DEFAULT NULL,
        	`rach_stp_att_large_msg` FLOAT NULL DEFAULT NULL,
        	`rach_stp_completions` FLOAT NULL DEFAULT NULL,
        	`transmit_tb_on_pch` FLOAT NULL DEFAULT NULL,
        	`transmit_tb_on_bch` FLOAT NULL DEFAULT NULL,
        	`transmit_tb_on_dl_sch` FLOAT NULL DEFAULT NULL,
        	`harq_retrans_on_dl_sch` FLOAT NULL DEFAULT NULL,
        	`corr_non_dupl_ul_sch_tb` FLOAT NULL DEFAULT NULL,
        	`corr_ul_sch_tb_re_recept` FLOAT NULL DEFAULT NULL,
        	`incorr_ul_sch_tb_recept` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs0` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs1` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs2` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs3` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs4` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs5` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs6` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs7` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs8` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs9` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs10` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs11` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs12` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs13` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs14` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs15` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs16` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs17` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs18` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs19` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs20` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs21` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs22` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs23` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs24` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs25` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs26` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs27` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_using_mcs28` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs0` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs1` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs2` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs3` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs4` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs5` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs6` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs7` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs8` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs9` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs10` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs11` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs12` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs13` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs14` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs15` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs16` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs17` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs18` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs19` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs20` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs21` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs22` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs23` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs24` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs25` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs26` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs27` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs28` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs0` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs1` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs2` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs3` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs4` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs5` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs6` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs7` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs8` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs9` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs10` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs11` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs12` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs13` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs14` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs15` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs16` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs17` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs18` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs19` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs20` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs21` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs22` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs23` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs24` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs25` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs26` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs27` FLOAT NULL DEFAULT NULL,
        	`pusch_trans_nack_mcs28` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs0` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs1` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs2` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs3` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs4` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs5` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs6` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs7` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs8` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs9` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs10` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs11` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs12` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs13` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs14` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs15` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs16` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs17` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs18` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs19` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs20` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs21` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs22` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs23` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs24` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs25` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs26` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs27` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs28` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_on_dl_dtch` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_on_dl_dcch` FLOAT NULL DEFAULT NULL,
        	`disc_sdu_on_dl_dtch` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_on_ul_dtch` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_on_ul_dcch` FLOAT NULL DEFAULT NULL,
        	`rlc_pdu_first_trans` FLOAT NULL DEFAULT NULL,
        	`rlc_pdu_re_trans` FLOAT NULL DEFAULT NULL,
        	`ul_rlc_pdu_dupl_rec` FLOAT NULL DEFAULT NULL,
        	`ul_rlc_pdu_retr_req` FLOAT NULL DEFAULT NULL,
        	`ul_rlc_pdu_disc` FLOAT NULL DEFAULT NULL,
        	`dl_ue_data_buff_avg` FLOAT NULL DEFAULT NULL,
        	`dl_ue_data_buff_max` FLOAT NULL DEFAULT NULL,
        	`ul_ue_data_buff_avg` FLOAT NULL DEFAULT NULL,
        	`ul_ue_data_buff_max` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_ul` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_dl` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_dl_disc` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs0` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs1` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs2` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs3` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs4` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs5` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs6` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs7` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs8` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs9` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs10` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs11` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs12` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs13` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs14` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs15` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs16` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs17` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs18` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs19` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs20` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs0` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs1` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs2` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs3` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs4` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs5` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs6` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs7` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs8` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs9` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs10` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs11` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs12` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs13` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs14` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs15` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs16` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs17` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs18` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs19` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs20` FLOAT NULL DEFAULT NULL,
        	`rrc_conn_ue_avg` FLOAT NULL DEFAULT NULL,
        	`rrc_conn_ue_max` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs21` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs22` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs23` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs24` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs25` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs26` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs27` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs28` FLOAT NULL DEFAULT NULL,
        	`dl_que_l_srb_min` FLOAT NULL DEFAULT NULL,
        	`dl_que_l_srb_avg` FLOAT NULL DEFAULT NULL,
        	`dl_que_l_srb_max` FLOAT NULL DEFAULT NULL,
        	`dl_que_l_drb_min` FLOAT NULL DEFAULT NULL,
        	`dl_que_l_drb_avg` FLOAT NULL DEFAULT NULL,
        	`dl_que_l_drb_max` FLOAT NULL DEFAULT NULL,
        	`dl_rlc_c_pdu_first_time` FLOAT NULL DEFAULT NULL,
        	`dl_rlc_d_pdu_first_time` FLOAT NULL DEFAULT NULL,
        	`dl_rlc_sdu_from_pdcp` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_bcch` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_dl_ccch` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_pcch` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_dl_dcch_disc` FLOAT NULL DEFAULT NULL,
        	`rlc_sdu_ul_ccch` FLOAT NULL DEFAULT NULL,
        	`ul_rlc_pdu_rececption` FLOAT NULL DEFAULT NULL,
        	`ul_rlc_pdu_rec_tot` FLOAT NULL DEFAULT NULL,
        	`cell_load_act_ue_avg` FLOAT NULL DEFAULT NULL,
        	`cell_load_act_ue_max` FLOAT NULL DEFAULT NULL,
        	`ue_drb_dl_data_qci_1` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_qci_1` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_qci_2` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_ul_qci_1` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_dl_qci_1` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_disc_dl_qci_1` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs0` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs1` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs2` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs3` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs4` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs5` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs6` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs7` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs8` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs9` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs10` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs11` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs12` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs13` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs14` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs15` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs16` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs17` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs18` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs19` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs20` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs21` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs22` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs23` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs24` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs25` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs26` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs27` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs28` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs0` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs1` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs2` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs3` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs4` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs5` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs6` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs7` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs8` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs9` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs10` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs11` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs12` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs13` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs14` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs15` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs16` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs17` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs18` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs19` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs20` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs21` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs22` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs23` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs24` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs25` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs26` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs27` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs28` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs0` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs1` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs2` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs3` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs4` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs5` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs6` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs7` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs8` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs9` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs10` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs11` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs12` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs13` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs14` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs15` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs16` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs17` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs18` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs19` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs20` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs21` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs22` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs23` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs24` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs25` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs26` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs27` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs28` FLOAT NULL DEFAULT NULL,
        	`ue_drb_dl_data_non_gbr` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_non_gbr` FLOAT NULL DEFAULT NULL,
        	`ue_drb_ul_data_qci_1` FLOAT NULL DEFAULT NULL,
        	`ue_drb_ul_data_non_gbr` FLOAT NULL DEFAULT NULL,
        	`pdcch_order_att` FLOAT NULL DEFAULT NULL,
        	`pdcch_init_order_att` FLOAT NULL DEFAULT NULL,
        	`pdcch_order_success` FLOAT NULL DEFAULT NULL,
        	`d_preamb_unavail` FLOAT NULL DEFAULT NULL,
        	`d_preamb_pdcch_unavail` FLOAT NULL DEFAULT NULL,
        	`d_preamb_ho_unavail` FLOAT NULL DEFAULT NULL,
        	`cell_load_ul_in_sync` FLOAT NULL DEFAULT NULL,
        	`cell_load_ul_in_sync_avg` FLOAT NULL DEFAULT NULL,
        	`cell_load_unl_pow_res` FLOAT NULL DEFAULT NULL,
        	`cell_load_ul_out_sync_0_05` FLOAT NULL DEFAULT NULL,
        	`cell_load_ul_out_sync_05_025` FLOAT NULL DEFAULT NULL,
        	`cell_load_ul_out_sync_025_10` FLOAT NULL DEFAULT NULL,
        	`cell_load_ul_out_sync_10_100` FLOAT NULL DEFAULT NULL,
        	`cell_load_ul_out_sync_100_inf` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs0` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs1` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs2` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs3` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs4` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs5` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs6` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs7` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs8` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs9` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs10` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs11` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs12` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs13` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs14` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs15` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs16` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs17` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs18` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs19` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs20` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs21` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs22` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs23` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs24` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs0` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs1` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs2` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs3` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs4` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs5` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs6` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs7` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs8` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs9` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs10` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs11` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs12` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs13` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs14` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs15` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs16` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs17` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs18` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs19` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs20` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs21` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs22` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs23` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs24` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs21` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs22` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs23` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs24` FLOAT NULL DEFAULT NULL,
        	`ue_drb_dl_data_qci_2` FLOAT NULL DEFAULT NULL,
        	`ue_drb_dl_data_qci_3` FLOAT NULL DEFAULT NULL,
        	`ue_drb_dl_data_qci_4` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_qci_3` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_qci_4` FLOAT NULL DEFAULT NULL,
        	`rach_stp_att_dedicated` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_dl_qci_2` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_dl_qci_3` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_dl_qci_4` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_disc_dl_qci_2` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_disc_dl_qci_3` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_disc_dl_qci_4` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs29` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs30` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_using_mcs31` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs29` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs30` FLOAT NULL DEFAULT NULL,
        	`pdsch_trans_nack_mcs31` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs29` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs30` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pdsch_mcs31` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs29` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs29` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs29` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs30` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs30` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs30` FLOAT NULL DEFAULT NULL,
        	`tb_bund2_nack_pdsch_mcs31` FLOAT NULL DEFAULT NULL,
        	`tb_bund3_nack_pdsch_mcs31` FLOAT NULL DEFAULT NULL,
        	`tb_bund4_nack_pdsch_mcs31` FLOAT NULL DEFAULT NULL,
        	`mean_prb_avail_pdsch` FLOAT NULL DEFAULT NULL,
        	`mean_prb_avail_pusch` FLOAT NULL DEFAULT NULL,
        	`num_rrc_conn_ue_avg` FLOAT NULL DEFAULT NULL,
        	`num_cell_load_act_ue_avg` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_ul` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_ul_qci_1` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_ul_qci_2` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_ul_qci_3` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_ul_qci_4` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_dl` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_dl_qci_1` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_dl_qci_2` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_dl_qci_3` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_loss_dl_qci_4` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_ul_qci_2` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_ul_qci_3` FLOAT NULL DEFAULT NULL,
        	`pdcp_sdu_ul_qci_4` FLOAT NULL DEFAULT NULL,
        	`active_ue_cat_1_avg` FLOAT NULL DEFAULT NULL,
        	`active_ue_cat_2_avg` FLOAT NULL DEFAULT NULL,
        	`active_ue_cat_3_avg` FLOAT NULL DEFAULT NULL,
        	`active_ue_cat_4_avg` FLOAT NULL DEFAULT NULL,
        	`active_ue_cat_5_avg` FLOAT NULL DEFAULT NULL,
        	`ca_dl_cap_ue_avg` FLOAT NULL DEFAULT NULL,
        	`ca_scell_conf_ue_avg` FLOAT NULL DEFAULT NULL,
        	`ca_scell_active_ue_avg` FLOAT NULL DEFAULT NULL,
        	`num_warn_etws_prim` FLOAT NULL DEFAULT NULL,
        	`num_warn_etws_sec` FLOAT NULL DEFAULT NULL,
        	`num_warn_cmas` FLOAT NULL DEFAULT NULL,
        	`sum_active_ue_data_dl` FLOAT NULL DEFAULT NULL,
        	`denom_active_ue_data_dl` FLOAT NULL DEFAULT NULL,
        	`sum_active_ue_data_ul` FLOAT NULL DEFAULT NULL,
        	`denom_active_ue_data_ul` FLOAT NULL DEFAULT NULL,
        	`sum_rrc_conn_ue` FLOAT NULL DEFAULT NULL,
        	`denom_rrc_conn_ue` FLOAT NULL DEFAULT NULL,
        	`sum_active_ue` FLOAT NULL DEFAULT NULL,
        	`denom_active_ue` FLOAT NULL DEFAULT NULL,
        	`time_cplane_ovl_l1` FLOAT NULL DEFAULT NULL,
        	`time_cplane_ovl_l2` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs25` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs26` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs27` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_mcs28` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs25` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs26` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs27` FLOAT NULL DEFAULT NULL,
        	`pusch_1st_trans_nack_mcs28` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs25` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs26` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs27` FLOAT NULL DEFAULT NULL,
        	`tb_bad_pusch_mcs28` FLOAT NULL DEFAULT NULL,
        	`ul_intra_comp_ue_avg` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_qci_5` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_qci_6` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_qci_7` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_qci_8` FLOAT NULL DEFAULT NULL,
        	`pdcp_ret_dl_del_mean_qci_9` FLOAT NULL DEFAULT NULL,
        	`sum_act_ue_sched_data_ul` FLOAT NULL DEFAULT NULL,
        	`denom_act_ue_sched_data_ul` FLOAT NULL DEFAULT NULL,
        	`sum_act_ue_sched_data_dl` FLOAT NULL DEFAULT NULL,
        	`denom_act_ue_sched_data_dl` FLOAT NULL DEFAULT NULL,
        	`ul_mu_mimo_paired_ue_avg` FLOAT NULL DEFAULT NULL,
        	`ca_dl_cap_ue_3cc_avg` FLOAT NULL DEFAULT NULL,
        	`ca_2scells_conf_ue_avg` FLOAT NULL DEFAULT NULL,
        	`ca_2scells_active_ue_avg` FLOAT NULL DEFAULT NULL,
        	`chng_to_cell_avail` FLOAT NULL DEFAULT NULL,
        	`chng_to_cell_plan_unavail` FLOAT NULL DEFAULT NULL,
        	`chng_to_cell_unplan_unavail` FLOAT NULL DEFAULT NULL,
        	`samples_cell_avail` FLOAT NULL DEFAULT NULL,
        	`samples_cell_plan_unavail` FLOAT NULL DEFAULT NULL,
        	`samples_cell_unplan_unavail` FLOAT NULL DEFAULT NULL,
        	`denom_cell_avail` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_01` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_02` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_03` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_04` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_05` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_06` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_07` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_08` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_09` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_10` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_11` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_12` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_13` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_14` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_15` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_16` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_17` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_18` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_19` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_20` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_21` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUSCH_LEVEL_22` FLOAT NULL DEFAULT NULL,
        	`NUM_CA_UE_SERV_CELL_AVG` FLOAT NULL DEFAULT NULL,
        	`NUM_CA_UE_SERV_CELL_MAX` FLOAT NULL DEFAULT NULL,
        	`NUM_NON_CA_UE_SERV_CELL_AVG` FLOAT NULL DEFAULT NULL,
        	`NUM_NON_CA_UE_SERV_CELL_MAX` FLOAT NULL DEFAULT NULL,
        	`DL_NGBR_IP_THR_DATA_CA_UE_2CC` FLOAT NULL DEFAULT NULL,
        	`DL_NGBR_IP_THR_T_CA_UE_2CC` FLOAT NULL DEFAULT NULL,
        	`RLC_PDU_DL_VOL_CA_PCELL` FLOAT NULL DEFAULT NULL,
        	`DL_CA_SCELL_DECONFIG_ATT` FLOAT NULL DEFAULT NULL,
        	`DL_CA_SCELL_DECONFIG_SUCC` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_01` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_02` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_03` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_04` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_05` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_06` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_07` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_08` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_09` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_10` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_11` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_12` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_13` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_14` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_15` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_16` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_17` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_18` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_19` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_20` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_21` FLOAT NULL DEFAULT NULL,
        	`RSSI_PUCCH_LEVEL_22` FLOAT NULL DEFAULT NULL,
        	PRIMARY KEY (xDate,xHour,OBJ_ID,MRBTS_ID,LNBTS_ID,LNCEL_ID))
        select * from isat_report.susy_4g_counter_hour;
        Drop table if EXISTS isat_report.susy_4g_counter_hour;
        ALTER TABLE isat_report.susy_4g_counter_hour_dummy RENAME TO  isat_report.susy_4g_counter_hour;
        """
    elif Request == "prbutil_daily":
        sqlscript_query = """
        REPLACE INTO isat_report.susy_pwi_prb_utilization
        SELECT xdate,xhour,a.MRBTS_ID,a.LNCEL_ID,a.OBJ_ID, dl_prb_util_tti_mean FROM isat_raw_4g.noklte_ps_lcellr_lncel_hour a WHERE a.xDate >=  '""" + yesterday_day.strftime("%Y-%m-%d") + "' and  dl_prb_util_tti_mean < 1000 "
    elif Request == "notifikasi_2g":
            sqlscript_query = """SELECT a.xDate,a.xhour, a.REGION, a.BAND,a.site_id,concat(a.BSC_ID,":",a.BCF_ID,":",a.BTS_ID) AS OBJ ,a.CELL_ID,a.MICRO_CLUSTER
            ,IFNULL(sum(CSSR_NUM),0) as CSSR_NUM
            ,IFNULL(sum(CSSR_DEN),0) as CSSR_DEN
            ,IFNULL(sum(TCH_Traffic_trf_24c),0) as TRAF
            FROM isat_report.susy_2gperfcell a
            """
    elif Request == "notifikasi_3g":
            sqlscript_query = """SELECT a.xdate, a.xhour, a.REGION, a.site_id, a.BAND, a.MICRO_CLUSTER,a.RNC_ID,a.WBTS_ID,a.WCEL_ID,CONCAT(a.RNC_ID,":",a.WBTS_ID,":",a.WCEL_ID) AS OBJ
            ,IFNULL(sum(CSSR_CS_NUM_RRC),0) as CSSR_CS_NUM_RRC
            ,IFNULL(sum(CSSR_CS_NUM_RAB),0) as CSSR_CS_NUM_RAB
            ,IFNULL(sum(CSSR_CS_DEN_RRC),0) as CSSR_CS_DEN_RRC
            ,IFNULL(sum(CSSR_CS_DEN_RAB),0) as CSSR_CS_DEN_RAB
            ,IFNULL(sum(CSSR_PS_NUM_RRC),0) as CSSR_PS_NUM_RRC
            ,IFNULL(sum(CSSR_PS_DEN_RRC),0) as CSSR_PS_DEN_RRC
            ,IFNULL(sum(CSSR_PS_NUM_RAB),0) as CSSR_PS_NUM_RAB
            ,IFNULL(sum(CSSR_PS_DEN_RAB),0) as CSSR_PS_DEN_RAB


            FROM isat_report.susy_3gperfcell a
            """
    elif Request == "notifikasi_4g":
            sqlscript_query = """SELECT a.xDate,a.xHour,a.site_id,a.BAND, a.MICRO_CLUSTER,a.MRBTS_ID,a.LNCEL_ID,CONCAT(a.MRBTS_ID,":",a.LNCEL_ID) AS OBJ
            ,SUM(a.`CSSR num1`) as CSSRNUM1
            ,SUM(a.`CSSR denum1`) as CSSRDENUM1
            ,SUM(a.`CSSR num2`) as CSSRNUM2
            ,SUM(a.`CSSR denum2`) as CSSRDENUM2
            ,SUM(a.`CSSR num3`) as CSSRNUM3
            ,SUM(a.`CSSR denum3`) as CSSRDENUM3
            ,SUM(a.`Total_Payload(MBytes)`) as `Total_Payload`

            FROM isat_report.susy_4Gperfcell_2 a
            """
    # elif Request == "notifikasi_2g_lock":
    #         sqlscript_query ="""SELECT b.xDate,b.SITE_ID,BTSNAME
    #         ,ROUND((SUM(b.CSSR_NUM)/SUM(b.CSSR_DENUM))*100,1) AS CSSR
    #         ,ROUND((SUM(b.DCR_NUM)/SUM(b.DCR_DENUM))*100,1) AS CDR
    #         ,ROUND((SUM(b.HOSR_NUM)/SUM(b.HOSR_DENUM))*100,1) AS HOSR
    #         FROM isat_report.susy_isat_2g_cell_day b """
    # elif Request == "notifikasi_4g_lock":
    #         sqlscript_query ="""SELECT b.xDate,b.SITE_ID,LNCELname
    #         ,ROUND((SUM(b.CSSR_NUM)/SUM(b.CSSR_DENUM))*100,1) AS CSSRPS
    #         ,ROUND((SUM(b.ERABDR_NUM)/SUM(b.ERABSR_DENUM))*100,1) AS CDRPS
    #         ,ROUND((SUM(b.INTRAFREQ_HOSR_NUM)/SUM(b.INTRAFREQ_HOSR_DENUM))*100,1) AS IntraHO
    #         FROM isat_report.susy_isat_4g_cell_day b  """
    # elif Request == "notifikasi_3g_lock":
    #         sqlscript_query ="""SELECT a.xDate,a.SITE_ID,WCELname
    #         ,round((sum(a.CSSRCS_NUM)/SUM(a.CSSRCS_DENUM))*100 ,1) AS CSSRCS
    #         ,ROUND(((SUM(a.CSSRPS1_NUM)/SUM(a.CSSRPS1_DENUM)*(sum(a.CSSRPS2_NUM)/SUM(a.CSSRPS2_DENUM))*(SUM(a.CSSRPS3_NUM)/SUM(a.CSSRPS3_DENUM)))+((SUM(a.CSSRPS4_NUM)/SUM(a.CSSRPS4_DENUM))*(SUM(a.CSSRPS5_NUM)/SUM(a.CSSRPS5_DENUM))))*100 ,1) AS CSSRPS
    #         ,round((SUM(a.CDRCS_NUM)/SUM(a.CDRCS_DENUM))*100 ,1) AS CDRCS
    #         ,round((SUM(a.CDRPS_NUM)/SUM(a.CDRPS_DENUM))*100 ,1) AS CDRPS
    #         ,round((SUM(a.SHO_NUM)/SUM(a.SHO_DENUM))*100 ,1) AS SHO
    #         FROM isat_report.susy_isat_3g_cell_day a  """

    return (sqlscript_query)
def getsqlpower(id1,id2,id3,id4,object_required):

    seminggulalu = datetime.date.today() - datetime.timedelta(hours =192)
    #=============================================================================================================
    if id1 != "" and id3 != "" and object_required == "BTS":
        sqlscript_queryBTS = """SELECT a.xdate,a.BSC,a.BCF,a.BTS, a.cellId as 'id' ,a.bcchTrxPower FROM isat_cm.bts a
        WHERE xdate >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND ((a.bsc = """ + str(id1) + """ AND a.BCF = """ + str(id2) + """) Or (a.bsc = """ + str(id3) + """ AND a.BCF = """ + str(id4) + """))
        """
    elif id1 != "" and id3 != "" and object_required == "TRX":
        sqlscript_queryBTS = """SELECT a.xdate,a.BSC,a.BCF,a.BTS,a.TRX,concat(a.BSC,"-",a.bcf,"-",a.bts,"-",a.TRX) AS 'id',a.trxRfPower FROM isat_cm.trx a
        WHERE xdate >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND ((a.bsc = """ + str(id1) + """ AND a.BCF = """ + str(id2) + """) Or (a.bsc = """ + str(id3) + """ AND a.BCF = """ + str(id4) + """))
        """
    elif id1 != "" and id3 == "" and object_required == "TRX":
        sqlscript_query = """SELECT a.xdate,a.BSC,a.BCF,a.BTS,a.TRX,concat(a.BSC,"-",a.bcf,"-",a.bts,"-",a.TRX) AS 'id',a.trxRfPower FROM isat_cm.trx a
        WHERE xdate >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND a.bsc = """ + str(id1) + """ AND a.BCF = """ + str(id2)
    elif id1 != "" and id3 == "" and object_required == "BTS":
        sqlscript_queryBTS = """SELECT a.xdate,a.BSC,a.BCF,a.BTS, a.cellId as 'id' ,a.bcchTrxPower FROM isat_cm.bts a
        WHERE xdate >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND a.bsc = """ + str(id1) + """ AND a.BCF = """ + str(id2)
    elif id1 == "" and id3 != "" and object_required == "TRX":
        sqlscript_query = """SELECT a.xdate,a.BSC,a.BCF,a.BTS,a.TRX,concat(a.BSC,"-",a.bcf,"-",a.bts,"-",a.TRX) AS 'id',a.trxRfPower FROM isat_cm.trx a
        WHERE xdate >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND a.bsc = """ + str(id3) + """ AND a.BCF = """ + str(id4)
    elif id1 == "" and id3 != "" and object_required == "BTS":
        sqlscript_queryBTS = """SELECT a.xdate,a.BSC,a.BCF,a.BTS, a.cellId as 'id' ,a.bcchTrxPower FROM isat_cm.bts a
        WHERE xdate >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND a.bsc = """ + str(id3) + """ AND a.BCF = """ + str(id4)


    elif id1 != "" and id3 != "" and object_required == "WCEL":
        sqlscript_queryBTS =""" SELECT a.xdate,a.rnc,a.wbts,a.WCEL  as 'id' ,a.PtxCellMax,a.MaxDLPowerCapability
        FROM isat_cm.wcel a WHERE a.xdate  >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND ((a.rnc = """ + str(id1) + """ AND a.wbts = """ + str(id2) + """) Or (a.rnc = """ +str(id3) + """ AND a.wbts = """ + str(id4) + """))
         """
    elif id1 != "" and id3 != "" and object_required == "LCELW":
        sqlscript_queryBTS =""" SELECT a.xdate,a.rnc,a.wbts,a.LCELW  as 'id' ,a.maxCarrierPower
        FROM isat_cm.LCELW a WHERE a.xdate  >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND ((a.rnc = """ + str(id1) + """ AND a.wbts = """ + str(id2) + """) Or (a.rnc = """ +str(id3) + """ AND a.wbts = """ + str(id4) + """))
         """
    elif id1 != "" and id3 == "" and object_required == "WCEL":
        sqlscript_queryBTS =""" SELECT a.xdate,a.rnc,a.wbts,a.WCEL  as 'id' ,a.PtxCellMax,a.MaxDLPowerCapability
        FROM isat_cm.wcel a WHERE a.xdate  >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND a.rnc = """ + str(id1) + """ AND a.wbts = """ + str(id2)
    elif id1 != "" and id3 == "" and object_required == "LCELW":
        sqlscript_queryBTS =""" SELECT a.xdate,a.rnc,a.wbts,a.LCELW as 'id' ,a.maxCarrierPower
        FROM isat_cm.LCELW a WHERE a.xdate  >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND a.rnc = """ + str(id1) + """ AND a.wbts = """ + str(id2)
    elif id1 == "" and id3 != "" and object_required == "WCEL":
        sqlscript_queryBTS =""" SELECT a.xdate,a.rnc,a.wbts,a.WCEL  as 'id' ,a.PtxCellMax,a.MaxDLPowerCapability
        FROM isat_cm.wcel a WHERE a.xdate >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        AND a.rnc = """ + str(id3) + """ AND a.wbts = """ + str(id4)
    elif id1 == "" and id3 != "" and object_required == "LCELW":
        sqlscript_queryBTS =""" SELECT a.xdate,a.rnc,a.wbts,a.LCELW as 'id' ,a.maxCarrierPower
        FROM isat_cm.LCELW a WHERE a.xdate >= '""" + seminggulalu.strftime("%Y-%m-%d")+ """'
        AND a.rnc = """ + str(id3) + """ AND a.wbts = """ + str(id4)

    elif id1 != "" and id2 != ""  and id3 != "" and object_required == "LNCEL":
        sqlscript_queryBTS =""" SELECT a.xdate,a.MRBTS,a.LNBTS,a.LNCEL,concat(a.MRBTS,a.LNCEL) as 'id',a.dlRsBoost,b.pMax FROM isat_cm.lncel_fdd a
        JOIN isat_cm.lncel b ON a.oss=b.oss and a.xdate = b.xdate and a.mrbts = b.mrbts and a.lncel = b.lncel
        WHERE a.xdate >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        and (a.mrbts =""" + str(id1) + """  or a.mrbts =""" + str(id2) + """  or a.mrbts =""" + str(id3) + """  )
        """
    elif id1 != "" and id2 != ""  and id3 == "" and object_required == "LNCEL":
        sqlscript_queryBTS =""" SELECT a.xdate,a.MRBTS,a.LNBTS,a.LNCEL,concat(a.MRBTS,a.LNCEL) as 'id',a.dlRsBoost,b.pMax FROM isat_cm.lncel_fdd a
        JOIN isat_cm.lncel b ON a.oss=b.oss and a.xdate = b.xdate and a.mrbts = b.mrbts and a.lncel = b.lncel
        WHERE a.xdate >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        and (a.mrbts =""" + str(id1) + """  or a.mrbts =""" + str(id2) + """  )
        """
    elif id1 != "" and id2 == ""  and id3 == "" and object_required == "LNCEL":
        sqlscript_queryBTS =""" SELECT a.xdate,a.MRBTS,a.LNBTS,a.LNCEL,concat(a.MRBTS,a.LNCEL) as 'id' ,a.dlRsBoost,b.pMax FROM isat_cm.lncel_fdd a
        JOIN isat_cm.lncel b ON a.oss=b.oss and a.xdate = b.xdate and a.mrbts = b.mrbts and a.lncel = b.lncel
        WHERE a.xdate  >= '""" + seminggulalu.strftime("%Y-%m-%d") + """'
        and (a.mrbts =""" + str(id1) + """)
        """

    return (sqlscript_queryBTS)
