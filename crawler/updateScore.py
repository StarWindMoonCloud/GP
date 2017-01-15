# Parse schedule
import json
import sys
import MySQLdb

def updateGameScore(game, db):
    updateCmd = "update SCHEDULE SET vscore = %s, hscore = %s where gid = %s"
    try:
        # Execute the SQL command
        cursor.execute(updateCmd, (game['vTeam']['score'], game['hTeam']['score'], game['gameId']))
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
    if 'games' in jsonSchedule:
        gameData = jsonSchedule['games']
        for game in gameData:
            updateGameScore(game, db)
# disconnect from server
db.close()