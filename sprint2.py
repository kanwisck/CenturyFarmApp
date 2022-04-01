import json
#from pykml import parser
#from os import path

aList = [
    {
        "farms": {
            "Chambers Farm": [
                {"lng": -123.0253000, "lat": 44.6488167},
                {"lng": -123.0340722, "lat": 44.6525139},
                {"lng": -123.0339972, "lat": 44.6543750},
                {"lng": -123.0221639, "lat": 44.6543417}
            ],
            "Dromgoole Farm": [
                {"lng": -123.1718394510763, "lat": 45.3609110216409},
                {"lng": -123.172029749661,  "lat": 45.35610258854292},
                {"lng": -123.1664837704136, "lat": 45.3560302361722},
                {"lng": -123.1626511100443, "lat": 45.3612393850841},
                {"lng": -123.1647286361762, "lat": 45.36137933389124},
                {"lng": -123.1643989695578, "lat": 45.36224477283911},
                {"lng": -123.1680455533266, "lat": 45.36223885899322},
                {"lng": -123.1686193059465, "lat": 45.36090854106052}
            ],
            "Bruck Farm": [
                {"lng": -122.7278229261364, "lat": 45.30645295190772},
                {"lng": -122.7186602463425, "lat": 45.30178845637814},
                {"lng": -122.7187759437213, "lat": 45.31016089964996},
                {"lng": -122.7277539750468, "lat": 45.30645295190772}
            ],
            "Freeman Family Farm": [
                {"lng": -123.2787515562552, "lat": 45.16480057879585},
                {"lng": -123.2780434181904, "lat": 45.16549568564049},
                {"lng": -123.2779039762229, "lat": 45.16674524535783},
                {"lng": -123.2803253888784, "lat": 45.16676915592996},
                {"lng": -123.2803516583018, "lat": 45.16708414985743},
                {"lng": -123.2779799333409, "lat": 45.16761990033132},
                {"lng": -123.2779597114043, "lat": 45.16858930624299},
                {"lng": -123.2806483673783, "lat": 45.16773322050761},
                {"lng": -123.2818974144741, "lat": 45.1676316021013},
                {"lng": -123.2819530782192, "lat": 45.16682134892718},
                {"lng": -123.2847729338458, "lat": 45.16683289551523},
                {"lng": -123.284716607415,  "lat": 45.16602598458444},
                {"lng": -123.2850171748228, "lat": 45.16599529030023},
                {"lng": -123.2848960877277, "lat": 45.16484272254449}
            ],
            "Delano Farms": [
                {"lat": 45.34976602696314, "lng": -122.4906612610669},
                {"lat": 45.34734844195968, "lng": -122.4890870351521},
                {"lat": 45.34696916300295, "lng": -122.4766555032135},
                {"lat": 45.34935933011464, "lng": -122.476657673228},
                {"lat": 45.34942613104019, "lng": -122.4812338951384},
                {"lat": 45.35601425369122, "lng": -122.4812874822723},
                {"lat": 45.35563182142811, "lng": -122.4860990798462},
                {"lat": 45.35516873474844, "lng": -122.4916948559063},
                {"lat": 45.35600860392447, "lng": -122.4916970105169},
                {"lat": 45.35585137306744, "lng": -122.4971030299542},
                {"lat": 45.35239805183505, "lng": -122.4970552896309},
                {"lat": 45.35254186412757, "lng": -122.4913170858831},
                {"lat": 45.34982994474439, "lng": -122.4908424095733},
                {"lat": 45.34976602696314, "lng": -122.4890687547992}
            ],
            "The Beitel Farm": [
                {"lat": 44.8278554054365, "lng": -122.7628299775307},
                {"lat": 44.81791990689522, "lng": -122.7629399785683},
                {"lat": 44.81793585246291, "lng": -122.7552838343676},
                {"lat": 44.82769631064512, "lng": -122.7555213762199},
                {"lat": 44.8278554054365, "lng": -122.7628299775307}
            ],
            "Select Seed Promised Seed": [
                {"lat": 45.11056587439315, "lng": -123.2682577145877},
                {"lat": 45.10945898694171, "lng": -123.2641387673533},
                {"lat": 45.11573445731704,  "lng": -123.264226241996},
                {"lat": 45.11557860463325, "lng": -123.2601760513648},
                {"lat": 45.11918282486616, "lng": -123.2601752798507},
                {"lat": 45.11930819825194, "lng": -123.2626676105758},
                {"lat": 45.12120355051001, "lng": -123.2626652528569},
                {"lat": 45.12127423608209, "lng": -123.2636652526741},
                {"lat": 45.12278092264365, "lng": -123.2636051627467},
                {"lat": 45.12258539863196, "lng": -123.2753648239075},
                {"lat": 45.116472841868333, "lng": -123.276054110991},
                {"lat": 45.11668769691688, "lng": -123.2790621746597},
                {"lat": 45.11081214063503, "lng": -123.2794497192028},
                {"lat": 45.11056587439315, "lng": -123.2682577145877}
            ],
            "Mullen Farms": [
                {"lat": 45.228131241,	"lng":-122.989806315},
	            {"lat": 45.226709879,   "lng":-122.988977489},		
	            {"lat": 45.224320981,   "lng":-122.989656814},		
	            {"lat": 45.224177944,   "lng":-122.958482691},		
	            {"lat": 45.234589515,   "lng":-122.958483520},		
	            {"lat": 45.234221153,   "lng":-122.950966000},		
	            {"lat": 45.234497377,   "lng":-122.947817846},		
	            {"lat": 45.233776731,   "lng":-122.946382270},		
	            {"lat": 45.234145666,   "lng":-122.946121143},		
	            {"lat": 45.239357189,   "lng":-122.955280216},		
	            {"lat": 45.232576909,   "lng":-122.964833367},		
	            {"lat": 45.230762545,   "lng":-122.967134104},		
	            {"lat": 45.228135403,   "lng":-122.968258606},		
	            {"lat": 45.228131241,   "lng":-122.989806315},
            ],
            "Tideman Johnson Farm": [
                {"lat": 45.463380202,   "lng": -122.623511914},	
                {"lat": 45.463738072,   "lng": -122.625717949},		
                {"lat": 45.462469310,   "lng": -122.625771331},		
                {"lat": 45.461276337,   "lng": -122.623816620},		
                {"lat": 45.460945347,   "lng": -122.621069013},		
                {"lat": 45.463796671,   "lng": -122.619896544},		
                {"lat": 45.463380202,   "lng": -122.623511914},
            ],
            "Voss Farms": [
                {"lat": 45.344336121,    "lng": -122.828323358},	
                {"lat": 45.342431421,    "lng": -122.828370325},		
                {"lat": 45.342485339,    "lng": -122.831094693},		
                {"lat": 45.344236449,    "lng": -122.831227303},		
                {"lat": 45.344335977,    "lng": -122.836071276},		
                {"lat": 45.336863195,    "lng": -122.836232960},		
                {"lat": 45.336301703,    "lng": -122.836186859},		
                {"lat": 45.336106641,    "lng": -122.829860454},		
                {"lat": 45.338913557,    "lng": -122.826190906},		
                {"lat": 45.339207354,    "lng": -122.824456062},		
                {"lat": 45.341142117,    "lng": -122.825948004},		
                {"lat": 45.344387786,    "lng": -122.825996983},		
                {"lat": 45.344336121,    "lng": -122.828323358},	
            ],
            "Haskin Heritage Century Farm": [
                {"lat": 44.50858650097742, "lng": -122.8656571641482}
            ],
            "Shady Brook Farm": [
                {"lat":  45.237954, "lng": -123.102738}
            ],
            "Bar M Ranch": [
                {"lat":  44.472232, "lng": -123.099577}
            ],
            "Oak Creek Farm": [
                {"lat":  44.478520, "lng": -122.880605}
            ],
            "Four Ridge Orchards": [
                {"lat":  45.424348, "lng": -123.007318}
            ],
            "Herring Farm": [
                {"lat":  45.311883, "lng": -123.020690}
            ],
            "Haslebacher Farms": [
                {"lat":  45.019848, "lng": -122.908823}
            ],
            "Stupfel Farm": [
                {"lat":  45.198436, "lng": -122.984627}
            ],
            "Cattrall Brothers Vineyards": [
                {"lat":  45.090944, "lng": -123.162414}
            ],
            "The Misner Family Farm": [
                {"lat":  44.634869, "lng": -122.906599}
            ],
            "Iwasaki Bros. Inc.": [
                {"lat":  45.501292, "lng": -122.966665}
            ],
            "Peter Fred Gossen Farm": [
                {"lat":  45.590375, "lng": -122.908860}
            ],
            "M. Christensen Family Farm, LLC": [
                {"lat":  45.133789, "lng": -123.271508}
            ],
            "Alder Glade Farm": [
                {"lat":  44.980899, "lng": -122.770134}
            ],
            "Mosby Century Farm": [
                {"lat":  43.781987, "lng": -122.998386}
            ],
            "Maple Hill Farm": [
                {"lat":  45.075112, "lng": -122.840758}
            ],
            "Jesse & Ruby Looney Farm": [
                {"lat":  44.753588, "lng": -123.016446}
            ],
            "Gordon Zimmerman Farm": [
                {"lat":  45.324885, "lng": -123.177172}
            ],
            "Smith Bros. Farms, LLC": [
                {"lat":  44.522904, "lng": -123.207757}
            ],
            "Gentleacres/Orion Farms": [
                {"lat":  44.860827, "lng": -123.237205}
            ],
            "Mid Valley Farm": [
                {"lat":  45.416350, "lng": -122.900065}
            ],
            "Christensen Farm": [
                {"lat":  44.280888, "lng": -123.070421}
            ],
            "Taghon Farm": [
                {"lat":  45.532212, "lng": -123.060562}
            ],
            "Fisher Patterson": [
                {"lat":  44.895447, "lng": -122.777044}
            ],
            "Hynes Farm": [
                {"lat":  45.050123, "lng": -122.867596}
            ],
            "Louis R. & Anna Falk Farm": [
                {"lat":  44.362760, "lng": -123.056456}
            ],
            "Charles Ludwig Falk Farm": [
                {"lat":  44.372268, "lng": -123.078142}
            ],
            "The Romig Ranch": [
                {"lat":  45.049030, "lng": -123.202956}
            ],
            "Plagmann Farms, Inc.": [
                {"lat":  44.657283, "lng": -122.951597}
            ],
            "Jansen Farm": [
                {"lat":  45.554103, "lng": -123.084298}
            ],
            "Three Branches, LLC": [
                {"lat":  45.341602, "lng": -123.226414}
            ],
            "Batchelder Farms, LLC": [
                {"lat":  45.589162, "lng": -122.947361}
            ],
            "VanDomelen Family Farm": [
                {"lat":  45.626693, "lng": -123.038364}
            ],
            "Three Oaks Farm": [
                {"lat":  45.200157, "lng": -123.116015}
            ],
            "Duck Inn Group, LLC": [
                {"lat":  45.092563, "lng": -122.904082}
            ],
            "AJ Strubhar Farm ": [
                {"lat":  45.184137, "lng": -122.765053}
            ],
            "Sam Luethe Farm": [
                {"lat":  45.605375, "lng": -122.838158}
            ],
            "Payne Farms": [
                {"lat":  45.260040, "lng": -123.157239}
            ],
            "McPhillips Farms Inc": [
                {"lat":  45.163932, "lng": -123.237324}
            ],
            "Hiebenthal Farms": [
                {"lat":  45.002677, "lng": -123.299946}
            ],
            "Fanning Farms": [
                {"lat":  45.070975, "lng": -123.296363}
            ],
            "Bierly Farm": [
                {"lat":  44.323703, "lng": -123.056517}
            ],
            "Bryon Scott Farms, Inc.": [
                {"lat":  44.522564, "lng": -123.111921}
            ],
            "Buzz Mitchell Farms": [
                {"lat":  44.568474, "lng": -122.912520}
            ],
            "Chambers Farm": [
                {"lat":  44.653408, "lng": -123.024828}
            ],
            "Montgomery Homestead Farm": [
                {"lat":  44.732773, "lng": -122.768135}
            ],
            "Hawley Land & Cattle Co.": [
                {"lat":  43.754222, "lng": -123.115768}
            ],
            "Dakota Heritage Ranch": [
                {"lat":  45.316358, "lng": -123.151386}
            ],
            "Goodrich Farm": [
                {"lat":  45.185201, "lng": -123.118728}
            ],
            "Silver Mountain Enterprises, LLC": [
                {"lat":  44.882534, "lng": -122.718024}
            ],
            "Richardson Farm": [
                {"lat":  44.129742, "lng": -123.302477}
            ],
            "Rice Ranch": [
                {"lat":  44.339541, "lng": -122.770838}
            ],
            "Jackson-Martinak Farm": [
                {"lat":  44.544599, "lng": -123.046902}
            ],
            "McKay Farms, Inc.": [
                {"lat":  45.196182, "lng": -122.936665}
            ],
            "McFarlane Farm": [
                {"lat":  45.369959, "lng": -122.492875}
            ],
            "Jack Vaughan Farm": [
                {"lat":  45.171955, "lng": -122.553226}
            ],
        }
    }
]

jsonString = json.dumps(aList)
jsonFile = open("farms.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

#kml_file = open('./kmlFiles/tideman.kml')
#with open(kml_file) as f:
#    doc = parser.parse(f).getroot()
#    print(root.Document.name)