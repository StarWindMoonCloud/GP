# Parse schedule
import json
import sys
import MySQLdb

def updateGameSchedule(game, db):
    insertCmd = "insert into SCHEDULE (gid, vtid, vtn, htid, htn, an, ac, etm) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        # Execute the SQL command
        cursor.execute(insertCmd, (str(game['gid']), str(game['v']['tid']), game['v']['tn'], str(game['h']['tid']), game['h']['tn'], game['an'], game['ac'], game['etm']))
        # Commit your changes in the database
        db.commit()
    except Exception, e:
        print str(e)
        # Rollback in case there is any error
        db.rollback()

db = MySQLdb.connect("localhost", "root", "", "gp")
cursor = db.cursor()


fileSchedule = sys.argv[1]
with open(fileSchedule) as data_file:
    jsonSchedule = json.load(data_file)
    #print jsonSchedule
    if 'lscd' in jsonSchedule:
        scheduleData = jsonSchedule['lscd']
        for monthSchedule in scheduleData:
            monthScheduleData = monthSchedule['mscd']
            for game in monthScheduleData['g']:
                updateGameSchedule(game, db)
# disconnect from server
db.close()