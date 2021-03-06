import android

data=[{'id':"92",'name':"Addison Road-Seat Pleasant"},
{'id':"85",'name':"Anacostia"},
{'id':"81",'name':"Archives-Navy Memorial-Penn Quarter"},
{'id':"42",'name':"Arlington Cemetery"},
{'id':"99",'name':"Ballston-MU"},
{'id':"90",'name':"Benning Road"},
{'id':"12",'name':"Bethesda"},
{'id':"47",'name':"Braddock Road"},
{'id':"89",'name':"Branch Ave"},
{'id':"27",'name':"Brookland-CUA"},
{'id':"91",'name':"Capitol Heights"},
{'id':"59",'name':"Capitol South"},
{'id':"66",'name':"Cheverly"},
{'id':"97",'name':"Clarendon"},
{'id':"8",'name':"Cleveland Park"},
{'id':"79",'name':"College Park-U of MD"},
{'id':"75",'name':"Columbia Heights"},
{'id':"86",'name':"Congress Heights"},
{'id':"96",'name':"Court House"},
{'id':"45",'name':"Crystal City"},
{'id':"65",'name':"Deanwood"},
{'id':"102",'name':"Dunn Loring-Merrifield"},
{'id':"6",'name':"Dupont Circle"},
{'id':"100",'name':"East Falls Church"},
{'id':"60",'name':"Eastern Market"},
{'id':"49",'name':"Eisenhower Avenue"},
{'id':"4",'name':"Farragut North"},
{'id':"38",'name':"Farragut West"},
{'id':"58",'name':"Federal Center SW"},
{'id':"53",'name':"Federal Triangle"},
{'id':"40",'name':"Foggy Bottom-GWU"},
{'id':"32",'name':"Forest Glen"},
{'id':"28",'name':"Fort Totten"},
{'id':"95",'name':"Franconia-Springfield"},
{'id':"11",'name':"Friendship Heights"},
{'id':"21",'name':"Gallery Pl-Chinatown"},
{'id':"76",'name':"Georgia Ave-Petworth"},
{'id':"34",'name':"Glenmont"},
{'id':"80",'name':"Greenbelt"},
{'id':"14",'name':"Grosvenor-Strathmore"},
{'id':"50",'name':"Huntington"},
{'id':"23",'name':"Judiciary Square"},
{'id':"48",'name':"King Street"},
{'id':"82",'name':"L'Enfant Plaza"},
{'id':"67",'name':"Landover"},
{'id':"109",'name':"Largo Town Center"},
{'id':"36",'name':"McPherson Square"},
{'id':"13",'name':"Medical Center"},
{'id':"1",'name':"Metro Center"},
{'id':"64",'name':"Minnesota Ave"},
{'id':"110",'name':"Morgan Boulevard"},
{'id':"70",'name':"Mt Vernon Sq 7th St-Convention Center"},
{'id':"84",'name':"Navy Yard"},
{'id':"87",'name':"Naylor Road"},
{'id':"68",'name':"New Carrollton"},
{'id':"108",'name':"New York Ave-Florida Ave-Gallaudet U"},
{'id':"43",'name':"Pentagon"},
{'id':"44",'name':"Pentagon City"},
{'id':"61",'name':"Potomac Ave"},
{'id':"78",'name':"Prince George's Plaza"},
{'id':"26",'name':"Rhode Island Ave-Brentwood"},
{'id':"17",'name':"Rockville"},
{'id':"93",'name':"Ronald Reagan Washington National Airport"},
{'id':"41",'name':"Rosslyn"},
{'id':"18",'name':"Shady Grove"},
{'id':"72",'name':"Shaw-Howard U"},
{'id':"31",'name':"Silver Spring"},
{'id':"54",'name':"Smithsonian"},
{'id':"107",'name':"Southern Avenue"},
{'id':"63",'name':"Stadium-Armory"},
{'id':"88",'name':"Suitland"},
{'id':"29",'name':"Takoma"},
{'id':"10",'name':"Tenleytown-AU"},
{'id':"16",'name':"Twinbrook"},
{'id':"73",'name':"U Street/African-Amer Civil War Memorial/Cardozo"},
{'id':"25",'name':"Union Station"},
{'id':"94",'name':"Van Dorn Street"},
{'id':"9",'name':"Van Ness-UDC"},
{'id':"103",'name':"Vienna/Fairfax-GMU"},
{'id':"98",'name':"Virginia Square-GMU"},
{'id':"83",'name':"Waterfront-SEU"},
{'id':"101",'name':"West Falls Church-VT/UVA"},
{'id':"77",'name':"West Hyattsville"},
{'id':"33",'name':"Wheaton"},
{'id':"15",'name':"White Flint"},
{'id':"7",'name':"Woodley Park-Zoo/Adams Morgan"}]


if __name__=='__main__':
	droid=android.Android()
	droid.dialogCreateAlert('Choose Station')
	stationlist=[i["name"] for i in data]
	droid.dialogSetItems(stationlist)
	droid.dialogShow()
	stationtemp=droid.dialogGetResponse().result["item"]
	stationid=data[stationtemp][id]
	print stationid
	droid.webViewShow('http://wmata.com/rider_tools/pids/showpid.cfm?station_id='+stationid)

