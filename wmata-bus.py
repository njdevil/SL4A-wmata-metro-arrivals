import android

if __name__=='__main__':
	droid=android.Android()
	stopid=droid.dialogGetInput('Bus Stop Number').result
	droid.webViewShow('http://wmata.nextbus.com/customStopSelector/adaPrediction.jsp?a=wmata&cssFile=http://www.wmata.com/css/nextbus.css?nocache&stopId='+stopid)
