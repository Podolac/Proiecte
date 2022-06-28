import random


def Generator_Nume(s):
    NUME_FAM = ["Abaza", "Adamache", "Adamescu", "Adameșteanu", "Aderca", "Adoc", "Afrim", "Agaparian", "Agârbiceanu",
                "Agîrbiceanu", "Albu", "Albu", "Albulescu", "Aldulescu", "Alexa", "Alexandrescu", "Alexe", "Alexi",
                "Alifantis", "Almășan", "Almaș", "Aman", "Amânar", "Andoni", "Andreoiu", "Andrieș", "Andronic",
                "Angelescu", "Anghel", "Anghelescu", "Anton", "Antonescu", "Apostu", "Ardelean", "Ardeleanu",
                "Argeșanu", "Argetoianu", "Arghezi", "Armășescu", "Arnăuțoiu", "Arnautu", "Arnăutu", "Asachi",
                "Athanasiu", "Averescu", "Avramescu", "Bacalbașa", "Baciu", "Baconschi", "Baconski", "Baconsky",
                "Bădărău", "Badea", "Bădescu", "Bădulescu", "Baghiu", "Baicu", "Bălăceanu", "Bălan", "Balanici",
                "Balauru", "Băloșescu", "Bălțat", "Bănățeanu", "Bănică", "Bănică", "Bănulescu", "Baracci", "Bărboianu",
                "Barbu", "Bărbuceanu", "Bărbulescu", "Bârcă", "Barcianu", "Bârlea", "Bârloiu", "Barna", "Bârsănescu",
                "Barzin", "Basarabeanu", "Bătrâneanu", "Bătrîneanu", "Bazon", "Bălașa", "Bălănescu", "Băsescu",
                "Bârlădeanu", "Becali", "Becheru", "Bechet", "Beclean", "Becșenescu", "Bega", "Begu", "Bejenaru",
                "Bejinariu", "Belcot", "Belgea", "Belimace", "Benga", "Bengescu", "Bentoiu", "Bercea", "Bercu",
                "Berghianu", "Berindei", "Besoiu", "Bibescu", "Bichineț", "Bîrlea", "Bîrloiu", "Bizău", "Blaga",
                "Bodescu", "Bodiu", "Bodiul", "Bodnăraș", "Bogos", "Bogza", "Bolliac", "Bonciu", "Borăscu", "Borcea",
                "Bordea", "Boroianu", "Bosânceanu", "Bosînceanu", "Boștină", "Botean", "Boteanu", "Botescu", "Botnari",
                "Botnaru", "Bozga", "Bozgă", "Bragadiru", "Braghiș", "Brâncoveanu", "Brănescu", "Brânzan", "Brânzeu",
                "Brașoveanu", "Brătescu", "Brateș", "Brătianu", "Bratu", "Brâncuși", "Breban", "Brediceanu", "Brega",
                "Brenduș", "Brezeanu", "Brînzan", "Broșteanu", "Brudașcu", "Brumaru", "Bucur", "Bucurescu", "Budeanu",
                "Budescu", "Buhagiar", "Buhuș", "Buia", "Bujor", "Bulacu", "Bulgari", "Bunea", "Bunescu", "Burada",
                "Burcă", "Burcea", "Burduja", "Burghele", "Burileanu", "Burtea", "Buruiană", "Buș", "Bușilă", "Buteanu",
                "Butnariu", "Butnaru", "Butoi", "Buzatu", "Buzdugan", "Buzescu", "Buzești", "Buzoianu", "Cămătaru",
                "Căciulescu", "Cacoveanu", "Cadanțu", "Căianu", "Căileanu", "Calimente", "Călina", "Călinescu",
                "Calotă", "Calotescu", "Călugăreanu", "Câmpeanu", "Câmpineanu", "Cândea", "Captaru", "Caraciobanu",
                "Caracostea", "Carafoli", "Caragiale", "Caragiani", "Caragiu", "Caramitru", "Caranfil", "Caranica",
                "Cardoș", "Carianopol", "Cărpiniș", "Cârțan", "Cartianu", "Casapu", "Casian", "Câșle", "Cassanovschi",
                "Cassian", "Cașu", "Catargi", "Catargiu", "Cățoiu", "Cătuneanu", "Căuș", "Cazacu", "Cazan", "Ceaușescu",
                "Ceaușu", "Cebanu", "Cebotari", "Cehanu", "Ceia", "Celan", "Celibidache", "Cenușaru", "Cepoi",
                "Cerăceanu", "Cernat", "Cernătescu", "Cernăianu", "Cernea", "Cernescu", "Cernovodeanu", "Cesereanu",
                "Chebac", "Chelaru", "Chelcea", "Chendi", "Chihaia", "Chindriș", "Chinezu", "Chintezanu", "Chioreanu",
                "Chira", "Chirilă", "Chirilov", "Chirnoagă", "Chirtoacă", "Chiru", "Chițu", "Ciceu", "Cihac",
                "Cimpoeșu", "Cîndea", "Cinteză", "Cioabă", "Cioacă", "Cioban", "Ciobanu", "Ciocâlteu", "Ciocârlan",
                "Cioculescu", "Ciolan", "Ciopraga", "Cioranu", "Ciorănescu", "Ciorbea", "Ciorogariu", "Cioroianu",
                "Ciortea", "Cipariu", "Cireșanu", "Ciubotaru", "Ciubuc", "Ciucă", "Ciuceanu", "Ciucurescu", "Ciulei",
                "Ciupe", "Ciupercovici", "Cîmpineanu", "Cleopa", "Coandă", "Cocea", "Cochinescu", "Cocoș", "Codreanu",
                "Codrescu", "Codruț", "Cojoc", "Cojocari", "Cojocaru", "Colceru", "Colibășanu", "Colțoiu", "Coman",
                "Comănescu", "Comarnescu", "Comănici", "Combiescu", "Comișel", "Conea", "Constantin", "Constantinescu",
                "Constantiniu", "Corban", "Corbea", "Corbu", "Cordoș", "Corduneanu", "Corfanta", "Cornea", "Cornea",
                "Corneanu", "Cornescu", "Corodeanu", "Coroi", "Coropcean", "Corut", "Corvin", "Cosma", "Cosmescu",
                "Cosmovici", "Coșovei", "Costea", "Costiniu", "Coșbuc", "Coșeriu", "Coteanu", "Cotescu", "Covaci",
                "Covaliu", "Covătaru", "Cozacovici", "Cozma", "Crăciun", "Crăciunescu", "Craiu", "Crăiniceanu",
                "Creangă", "Crețu", "Crisbășan", "Cristea", "Cristescu", "Crișan", "Croitor", "Croitoru", "Cucu",
                "Culianu", "Cuparencu", "Cupcea", "Cupșa", "Cusin", "Cuza", "Damaschin", "Dănceanu", "Danciu",
                "Dănciulescu", "Dănescu", "Dănișor", "Dăscălescu", "Dascălu", "Datcu", "Gheorghe", "David",
                "Davidovici", "Dărănuța", "Deac", "Dediu", "Dejeu", "De", "la", "Marina", "Deleanu", "Demetrescu",
                "Derdena", "Diaconu", "Diculescu", "Dinculeanu", "Dinescu", "Dinică", "Dinicu", "Dinu", "Dinulescu",
                "Diță", "Djuvara", "Dobra", "Dobran", "Dobrin", "Dobrescu", "Dobrincu", "Dobrițoiu", "Dobrogeanu",
                "Dobrogianu", "Dobroiu", "Dogariu", "Dogaru", "Doicaru", "Doinaș", "Dolănescu", "Dolgan", "Dolha",
                "Donici", "Donțul", "Dorneanu", "Dorobanțu", "Drăgan", "Drăgănescu", "Drăganu", "Drăghiceanu",
                "Drăghicescu", "Drăghici", "Draghincescu", "Dragnea", "Dragomirescu", "Dragoș", "Dragu", "Drăgulescu",
                "Drăguș", "Drăgușanu", "Drăgușeanu", "Drăgoi", "Drosu", "Drugănescu", "Ducas", "Dugulescu", "Dulgheru",
                "Dumbrăveanu", "Dumitrescu", "Dumitru", "Dzițac", "Edeleanu", "Eliade", "Eminescu", "Enache", "Ene",
                "Enescu", "Epureanu", "Erbiceanu", "Eșanu", "Esinencu", "Făgăraș", "Făgărășanu", "Familia", "Rațiu",
                "Familia", "Trancu", "Fătu", "Frențiu", "Fernic", "Fieraru", "Filimon", "Filipescu", "Filotti",
                "Finiti", "Firulescu", "Flondor", "Florea", "Stanciu", "Florescu", "Florianu", "Fluieraș", "Foarță",
                "Focșăneanu", "Focșanu", "Focșeneanu", "Focșineanu", "Fotino", "Frățila", "Frosin", "Frunda", "Fugaru",
                "Fulga", "Gafița", "Găitan", "Gălățanu", "Galeriu", "Ganea", "Găvănescu", "Găină", "Gănescu",
                "Geambașu", "Geiculescu", "Georgescu", "Gheorghe", "Gheorghelaș", "Gheorghilaș", "Gheorghiu",
                "Gherghel", "Gherghescu", "Ghideanu", "Ghinea", "Ghiță", "Ghizari", "Gigurtu", "Gingăraș", "Giosanu",
                "Giurescu", "Gliga", "Gligor", "Glogoveanu", "Goanța", "Godea", "Goga", "Goian", "Gojdu", "Gojnea",
                "Goldiș", "Goma", "Gondi", "Gozsdu", "Grădișteanu", "Grebencea", "Greceanu", "Grecescu", "Grecu",
                "Grigorescu", "Grigoriu", "Grindea", "Gritti", "Grosescu", "Groșescu", "Grosu", "Groza", "Grozescu",
                "Gruia", "Gruia", "Gruiescu", "Guci", "Gulian", "Gușă", "Gușatu", "Guțiu", "Guțu", "Hagi", "Halep",
                "Halippa", "Hanganu", "Hanu", "Hasdeu", "Hațieganu", "Herescu", "Herlea", "Hermeneanu", "Herța",
                "Hertza", "Hetco", "Hirțea", "Hoban", "Hodorogea", "Hodoș", "Hodoș", "Holda", "Honcescu", "Hossu",
                "Hrisoverghi", "Hristu", "Huidu", "Huniade", "Hurezeanu", "Hurmuzescu", "Iacobescu", "Iaru", "Ierunca",
                "Iliescu", "Inculeț", "Ionel", "Ionesco", "Ionescu", "Ionică", "Ioniță", "Iordache", "Iordăchescu",
                "Ioviță", "Ioviț", "Irimescu", "Irimia", "Irimie", "Isopescu", "Ispas", "Istrati", "Ivănceanu",
                "Ivănescu", "Ivașcu", "Ivasiuc", "Izbașa", "Jean", "Mihail", "Jebeleanu", "Joldea", "Josan", "Jumanca",
                "Kiazim", "Kirițescu", "Kogălniceanu", "Lăcătuș", "Lăcustă", "Lahovary", "Lambru", "Lascăr", "Lascu",
                "Laurian", "Lăzăreanu", "Lazu", "Lăzureanu", "Lăzărescu", "Leca", "Lecca", "Lepădatu", "Liiceanu",
                "Lincar", "Lipă", "Lipatti", "Livescu", "Livezeanu", "Logothetti", "Loghin", "Loteanu", "Lotru",
                "Lovinescu", "Lubanovici", "Luca", "Lucaciu", "Lucan", "Lucescu", "Luchian", "Lugojan", "Lugojanu",
                "Lungu", "Lup", "Lupan", "Lupașcu", "Lupea", "Lupescu", "Lupșan", "Lupu", "Lupu", "Lupul", "Lupulescu",
                "Lupuțiu", "Mânea", "Macovei", "Macri", "Magheru", "Măgureanu", "Maican", "Mailat", "Mălăncioiu",
                "Malcoci", "Maluțan", "Manciulea", "Manea", "Mănescu", "Manicatide", "Manoilă", "Manole", "Manolescu",
                "Manțog", "Mărăcuță", "Mărăscu", "Mărășescu", "Marchitan", "Mardare", "Mărginean", "Mărgineanu",
                "Marin", "Marinescu", "Marioțeanu", "Mavrodin", "Măzărachi", "Mazilu", "Nicolae", "Mărgineanu",
                "Medeleanu", "Meleșcanu", "Melinte", "Miclăuș", "Micle", "Miclea", "Miclescu", "Miculescu", "Mihăescu",
                "Mihăileanu", "Mihăiță", "Mihaiu", "Mihalache", "Mihăilă", "Mihăilescu", "Mihnea", "Minovici", "Mircea",
                "Mironescu", "Mișu", "Mitu", "Mitu", "Mocănescu", "Mocanu", "Moceanu", "Mocioni", "Moculescu",
                "Modorcea", "Möller", "Mogoș", "Moiș", "Moldovan", "Moldoveanu", "Morar", "Moroșanu", "Morțun",
                "Moscopol", "Moscovici", "Motiș", "Motoc", "Moțoc", "Motrescu", "Moța", "Movilă", "Movileanu", "Mugur",
                "Muntean", "Munteanu", "Murafa", "Murărescu", "Muraru", "Mureșanu", "Mureșan", "Murgeanu", "Murgescu",
                "Murgoci", "Murguleț", "Murnu", "Mușat", "Muscalu", "Muscă", "Naghi", "Năstase", "Neacșu", "Neaga",
                "Neagoe", "Neagu", "Neamțu", "Nechita", "Nichita", "Necula", "Neculai", "Neculce", "Negoiță",
                "Negoițescu", "Negrea", "Negreanu", "Negrescu", "Negru", "Nemescu", "Neniță", "Nica", "Nicoară",
                "Nicolaescu", "Nicolaie", "Nicolau", "Nicolescu", "Nicu", "Niculae", "Niculescu", "Nicușor", "Nistor",
                "Niță", "Nițescu", "Noica", "Notara", "Nottara", "Oancea", "Râul", "Oancea", "Odobescu", "Oeriu",
                "Ogăraru", "Oișteanu", "Olănescu", "Olari", "Olariu", "Olaru", "Olinescu", "Oltean", "Olteanu", "Onaca",
                "Onciu", "Onoriu", "Oprea", "Oprescu", "Opriș", "Oprișan", "Orașan", "Orășan", "Orășanu", "Orăscu",
                "Orășean", "Orășeanu", "Orleanu", "Ornea", "Oroveanu", "Pacepa", "Pâclișan", "Pâclișanu", "Păcurariu",
                "Păcuraru", "Pădurariu", "Păduraru", "Pădureanu", "Paduretu", "Pădurețu", "Panaitescu", "Pană",
                "Pangrati", "Panțuru", "Papacioc", "Papacostea", "Papahagi", "Papură", "Parascan", "Parghel",
                "Parizescu", "Partoș", "Pârvu", "Pascali", "Pascaly", "Pașcanu", "Pascu", "Pâslaru", "Pastia", "Pașcu",
                "Pătraș", "Pătrașcu", "Patriciu", "Pătruț", "Păun", "Drumur", "Pavelescu", "Păturică", "Păun",
                "Păunescu", "Pârvulescu", "Pella", "Pellea", "Penescu", "Pescaru", "Petcu", "Petrașcu", "Petre",
                "Petrescu", "Petriceicu", "Petruț", "Picior", "Piersic", "Pietraru", "Pintilie", "Pîslaru", "Pitulea",
                "Pițurcă", "Pleșan", "Ploeșteanu", "Ploieșteanu", "Podoleanu", "Podriga", "Poenaru", "Poghirc",
                "Pogonat", "Pogoneanu", "Pogor", "Poienaru", "Pomuț", "Pop", "Popa", "Popea", "Popescu", "Popovici",
                "Popoviciu", "Poroineanu", "Porumbescu", "Posea", "Posteucă", "Postolache", "Preda", "Predescu",
                "Predoiu", "Prelipceanu", "Preoteasa", "Proca", "Procopie", "Procopovici", "Puiu", "Purcărete",
                "Pușcariu", "Pușcaș", "Pușcașu", "Puşcaşu", "Puțuri", "Răceanu", "Racoți", "Racoveanu", "Racoviță",
                "Rădescu", "Rădoi", "Radovanu", "Radovici", "Radu", "Răducan", "Răducanu", "Răducioiu", "Răduță",
                "Râpeanu", "Rațiu", "Răzvan", "Rădulescu", "Rebengiuc", "Rebreanu", "Ressu", "Rîpă", "Rîpeanu", "Roată",
                "Robu", "Rogoz", "Romanescu", "Rosetti", "Roșca", "Rotariu", "Rotaru", "Rudeanu", "Runceanu", "Rus",
                "Rușanu", "Rusca", "Rusescu", "Russo", "Rusu", "Sabău", "Sachelarie", "Sadoveanu", "Săhleanu",
                "Șăineanu", "Sănătescu", "Șandru", "Sandu", "Sânmărtean", "Sărățeanu", "Sârghie", "Sasu", "Sătmăreanu",
                "Săulescu", "Săvescu", "Savin", "Săceanu", "Săftoiu", "Sârbu", "Scarlat", "Șcurea", "Sechelariu",
                "Seciu", "Șelmaru", "Șerb", "Șchiopul", "Șerban", "Șerbănescu", "Șerbănoiu", "Șerbu", "Șerbulescu",
                "Seulescu", "Sihleanu", "Silaș", "Simionescu", "Simu", "Șirato", "Sireteanu", "Sirețeanu", "Sîrghie",
                "Sirma", "Skutnik", "Slavici", "Smochină", "Soare", "Socolescu", "Solacolu", "Șoldea", "Soltan",
                "Someșan", "Sorescu", "Sorohan", "Spădaru", "Spătaru", "Spineanu", "Spircu", "Spîrlea", "Stamatin",
                "Stamatu", "Stan", "Stanca", "Stancu", "Stănculescu", "Stavarache", "Stănescu", "Ștefănescu",
                "Ștefănucă", "Șteflea", "Ștefureac", "Stelian", "Știrbei", "Stoenescu", "Stoian", "Stolnici",
                "Străjescu", "Strătilescu", "Stroe", "Stroescu", "Stroici", "Sturdza", "Sturza", "Suceveanu", "Suciu",
                "Surdu", "Șușman", "Șchiopu", "Tabăra", "Tăbăraș", "Talianu", "Tămaș", "Tapalagă", "Țăranu",
                "Tăriceanu", "Tatomirescu", "Tavitian", "Tănase", "Tănăsescu", "Teleanu", "Țenescu", "Teodorașcu",
                "Teodorescu", "Teodosiu", "Țepeneag", "Tescanu", "Tighineanu", "Timică", "Timofte", "Timofti", "Țîrle",
                "Tiron", "Tismăneanu", "Țițeica", "Todea", "Toderaș", "Todiraș", "Todoran", "Toduță", "Toma", "Tomița",
                "Tomoiagă", "Toneanu", "Topor", "Torje", "Trandafir", "Trașcă", "Trifa", "Trifan", "Trifu", "Tudan",
                "Tudor", "Tudorache", "Tudoran", "Tudose", "Tuducan", "Țulea", "Turcan", "Țurcan", "Țurcanu",
                "Turcescu", "Turcu", "Turdeanu", "Țuțea", "Tutoveanu", "Udilă", "Udrea", "Uglar", "Ulmeanu", "Ungheanu",
                "Ungur", "Ungureanu", "Urs", "Ursăchianu", "Urziceanu", "Văcăroiu", "Vădineanu", "Văduva", "Vâlcu",
                "Văleanu", "Văluță", "Vânătoru", "Vanghelie", "Varo", "Varzar", "Văsescu", "Vasilescu", "Vasiliu",
                "Vatamanu", "Vântu", "Vellescu", "Vernescu", "Vianu", "Vicoveanca", "Videanu", "Vîlcu", "Vindereu",
                "Vințan", "Vioreanu", "Vitcu", "Vlădescu", "Vladimirescu", "Vladu", "Vlahuță", "Vlaicu", "Vlasiu",
                "Vlădărău", "Voicu", "Voiculescu", "Voiculeț", "Voina", "Voinea", "Voinescu", "Vraca", "Vulcan",
                "Vulcănescu", "Vulpe", "Vulpescu", "Xenopol", "Zaharescu", "Zaharia", "Zărnescu", "Zavati", "Zavoda",
                "Zăvoranu", "Zbenghea", "Zegrean", "Zegreanu", "Zgondea", "Zidaru", "Zlotea", "Zorlescu", "Zotta",
                "Zugrăvescu"]
# 1160 nume familie

    PRENUME_B = ["Abel", "Achim", "Adam", "Adelin", "Adi", "Adonis", "Adrian", "Agnos", "Albert", "Aleodor", "Alex",
                 "Alexandru", "Alexe", "Alin", "Alistar", "Amedeu", "Amza", "Anatolie", "Andrei", "Andrian", "Angel",
                 "Anghel", "Antim", "Anton", "Antonie", "Antoniu", "Arcadian", "Arian", "Aristide", "Arsenie",
                 "Atanasio", "Augustin", "Aurel", "Aurelian", "Aurică", "Avram", "Axinte", "Barbu", "Bartolomeu",
                 "Basarab", "Bănel", "Bebe", "Beniamin", "Benone", "Bernard", "Bogdan", "Brăduț", "Bucur", "Caius",
                 "Camil", "Cantemir", "Carol", "Casian", "Cazimir", "Călin", "Cătălin", "Cecil", "Cedrin", "Cezar",
                 "Ciprian", "Claudiu", "Codin", "Codrin", "Codruț", "Constantin", "Cornel", "Corneliu", "Corvin",
                 "Cosmin", "Costache", "Costică", "Costel", "Costin", "Crin", "Cristea", "Cristian", "Cristinel",
                 "Cristobal", "Cristofor", "Dacian", "Damian", "Dan", "Daniel", "Darius", "David", "Decebal", "Denis",
                 "Dinu", "Dionisie", "Dominic", "Dorel", "Dorian", "Dorin", "Dorinel", "Doru", "Dragomir", "Dragoș",
                 "Ducu", "Dumitru", "Edgar", "Edmond", "Eduard", "Eftimie", "Emanoil", "Emanuel", "Emanuil", "Emil",
                 "Emilian", "Eremia", "Eric", "Ernest", "Eugen", "Eusebiu", "Eustațiu", "Fabian", "Felix", "Filip",
                 "Fiodor", "Flaviu", "Florea", "Florentin", "Florian", "Florin", "Francisc", "Gabi", "Gabriel", "Gelu",
                 "George", "Georgel", "Georgian", "Ghenadie", "Gheorghe", "Gheorghiță", "Gherasim", "Ghiță", "Gică",
                 "Gicu", "Giorgian", "Grațian", "Gregorian", "Grigoraș", "Grigore", "Haralamb", "Haralambie", "Horațiu",
                 "Horea", "Horia", "Horică", "Iacob", "Iacov", "Iancu", "Ianis", "Ieremia", "Ilarie", "Ilarion", "Ilie",
                 "Iliuță", "Inocențiu", "Ioan", "Ion", "Ionel", "Ionică", "Ioniță", "Ionuț", "Iorgu", "Iosif", "Irinel",
                 "Isidor", "Iulian", "Iuliu", "Iurie", "Iustin", "Iustinian", "Ivan", "Jan", "Jean", "Jenel",
                 "Ladislau", "Lascăr", "Laurențiu", "Laurian", "Lazăr", "Leonard", "Leontin", "Leordean", "Lică",
                 "Liviu", "Lorin", "Luca", "Lucențiu", "Lucian", "Lucrețiu", "Ludovic", "Manole", "Marcel", "Marcu",
                 "Marian", "Marin", "Marinel", "Marius", "Martin", "Matei", "Maxim", "Maximilian", "Mădălin", "Mihai",
                 "Mihail", "Mihăiță", "Mihnea", "Mina", "Mircea", "Miron", "Mitică", "Mitruț", "Moise", "Mugur",
                 "Mugurel", "Nae", "Narcis", "Nechifor", "Nelu", "Nichifor", "Nicoară", "Nicodim", "Nicolae",
                 "Nicolaie", "Nicu", "Niculiță", "Nicușor", "Nicuță", "Norbert", "Noris", "Norman", "Octav",
                 "Octavian", "Octaviu", "Olimpian", "Olimpiu", "Oliver", "Oliviu", "Ovidiu", "Pamfil", "Panagachie",
                 "Panait", "Paul", "Pavel", "Pătru", "Petre", "Petrică", "Petrișor", "Petru", "Petruț", "Pintiliu",
                 "Pleșu", "Pompiliu", "Radu", "Rafael", "Rareș", "Raul", "Răducu", "Răzvan", "Relu", "Remus", "Robert",
                 "Romeo", "Romi", "Romică", "Romulus", "Sabin", "Sandu", "Sandu", "Sava", "Sebastian", "Septimiu",
                 "Sergiu", "Sever", "Severin", "Silvian", "Silviu", "Simi", "Simion", "Sinică", "Sorin", "Stan",
                 "Stancu", "Stelian", "Șerban", "Ștefan", "Teodor", "Teofil", "Teohari", "Theodor", "Tiberiu",
                 "Timotei", "Titus", "Todor", "Toma", "Traian", "Trandafir", "Tudor", "Valentin", "Valer", "Valeriu",
                 "Valter", "Vasile", "Vasilică", "Veniamin", "Vicențiu", "Victor", "Vincențiu", "Viorel", "Visarion",
                 "Virgil", "Vlad", "Vladimir", "Vlaicu", "Voicu", "Zamfir", "Zeno", "Zaharia "]
# 320 nume baieti

    PRENUME_F = ["Adelina", "Adina", "Adriana", "Adela", "Agnes", "Alina", "Alexandra", "Ana", "Anastasia", "Anisoara",
                 "Ana-Maria", "Anca", "Angelica", "Andreea", "Andra", "Antonia", "Aurora", "Aura", "Aurelia", "Bogdana",
                 "Brandusa", "Bianca", "Camelia", "Carina", "Cezara", "Cecilia", "Crina", "Cosmina", "Codruta", "Clara",
                 "Carmen", "Catalina", "Carla", "Cristina", "Cristiana", "Claudia", "Corina", "Daciana", "Doina",
                 "Dorina", "Dalia", "Dana", "Daniela", "Daria", "Delia", "Diana", "Ecaterina", "Elena", "Elisabeta",
                 "Eliza", "Emilia", "Ema", "Florentina", "Felicia", "Gabriela", "Geanina", "Georgiana", "Gloria",
                 "Gratiela", "Gina", "Greta", "Ilinca", "Ioana", "Irina", "Iulia", "Izabela", "Iris", "Lacramioara",
                 "Laura", "Lavinia", "Larisa", "Letitia", "Liliana", "Lidia", "Luiza", "Lucia", "Luminita", "Madalina",
                 "Mara", "Marcela", "Maria", "Mariana", "Melania", "Mihaela", "Mirela", "Mirabela", "Monica", "Mioara",
                 "Nadia", "Narcisa", "Nicoleta", "Nina", "Natasa", "Oana", "Ozana", "Otilia", "Olimpia", "Olivia",
                 "Paula", "Raluca", "Ramona", "Rodica", "Romanita", "Roxana", "Ruxandra", "Sabina", "Silvia", "Simona",
                 "Sofia", "Sonia", "Stela", "Sorina", "Sorana", "Stefania", "Selena", "Selina", "Simina", "Tatiana",
                 "Tereza", "Teodora", "Tamara", "Tania", "Valentina", "Violeta", "Victoria", "Viorela", "Virginia",
                 "Viviana", "Zoe", "Constanta", "Petronela", "Jana", "Joita", "Ileana", "Dochia", "Draga", "Chira",
                 "Eufrozina", "Fevronia", "Crenguta", "Margareta", "Niculina", "Stana", "Vasilica", "Zamfira", "Dafina",
                 "Smaranda", "Sanda", "Serafima", "Matilda", "Iustina", "Agripina", "Ivona", "Hortensia", "Elvira",
                 "Afina", "Dumbravita", "Cornelia", "Vasilica", "Ioana", "Ionica", "Ionela", "Antonia", "Antoaneta",
                 "Antoanela", "Veronica", "Vera", "Agata", "Valentina", "Teodora", "Teo", "Casiana", "Alexia",
                 "Iosefina", "Gabriela", "Gabi", "Georgiana", "Georgeta", "Georgina", "Geta", "Gheorgita", "Irina",
                 "Elena", "Ileana", "Lenuta", "Leana", "Constanta", "Constantina", "", "Tina", "Iulia", "Iuliana",
                 "Petronela", "Petra", "Petruta", "Paula", "Stefania", "Stefana", "Emilia", "Emiliana", "Ilinca",
                 "Ilia", "Magdalena", "Magda", "Ana", "Anisoara", "Anita", "Ancuta", "Laura", "Maria", "Mariana",
                 "Maia", "Mioara", "Adriana", "Adina", "Natalia", "Alexandra", "Sanda", "Sandra", "Elisabeta",
                 "Elizabeta", "Eliza", "Liliana", "Izabela", "Dumitra", "Dumitrita", "Mihaela", "Gabriela", "Gabi",
                 "Andreea", "Nicoleta", "Cristina", "Cristiana", "Crista", "Filofteia", "Filoftea", "Agripina",
                 "Paraschiva", "Tatiana", "Eufrasia", "Daria", "Ilaria", "Lidia", "Zenaida", "Lucia"]
# 245 nume fete

    if s == 1 or s == 5:
        NUME_GEN = (NUME_FAM[random.randint(0, 1159)])
        PRENUME_GEN = PRENUME_B[random.randint(0, 319)]
        return NUME_GEN + " " + PRENUME_GEN
    elif s == 2 or s == 6:
        NUME_GEN = (NUME_FAM[random.randint(0, 1159)])
        PRENUME_GEN = PRENUME_F[random.randint(0, 244)]
        return NUME_GEN + " " + PRENUME_GEN


def Generator_CNP():
    if random.randint(0, 1):
        S = random.randint(5, 6)
    else:
        S = random.randint(1, 2)
    AA = random.randint(0, 99)
    LL = random.randint(1, 12)
    if ((AA % 4 == 0 and AA % 100 != 0) or AA % 400) and LL == 2:
        ZZ = random.randint(1, 29)
    elif LL == 2:
        ZZ = random.randint(1, 28)
    elif LL == 1 or LL == 3 or LL == 5 or LL == 7 or LL == 8 or LL == 10 or LL == 12:
        ZZ = random.randint(1, 31)
    else:
        ZZ = random.randint(1, 30)
    JJ = random.randint(1, 52)
    NNN = random.randint(1, 999)
    VER_C = (S * 2 + (AA // 10) * 7 + (AA % 10) * 9 + (LL // 10) * 1 + (LL % 10) * 4 + (ZZ // 10) * 6 + (ZZ % 10) * 3
             + (JJ // 10) * 5 + (JJ % 10) * 8 + (NNN // 100) * 2 + (NNN % 100 // 10) * 7 + (NNN % 10) * 9) % 11
    if VER_C < 10:
        C = VER_C
    else:
        C = 1
    CNP = (S * 10 ** 12) + (AA * 10 ** 10) + (LL * 10 ** 8) + (ZZ * 10 ** 6) + (JJ * 10 ** 4) + (NNN * 10) + C
    return CNP


def Generator_CNP_D(s, jj):

    if s == 5 or s == 6:
        AA = random.randint(0, 20)
    else:
        AA = random.randint(0, 99)

    LL = random.randint(1, 12)

    if ((AA % 4 == 0 and AA % 100 != 0) or AA % 400) and LL == 2:
        ZZ = random.randint(1, 29)
    elif LL == 2:
        ZZ = random.randint(1, 28)
    elif LL == 1 or LL == 3 or LL == 5 or LL == 7 or LL == 8 or LL == 10 or LL == 12:
        ZZ = random.randint(1, 31)
    else:
        ZZ = random.randint(1, 30)

    if jj == 41:
        jj = 51
    elif jj == 42:
        jj = 52

    NNN = random.randint(1, 999)

    VER_C = (s * 2 + (AA // 10) * 7 + (AA % 10) * 9 + (LL // 10) * 1 + (LL % 10) * 4 + (ZZ // 10) * 6 + (ZZ % 10) * 3
             + (jj // 10) * 5 + (jj % 10) * 8 + (NNN // 100) * 2 + (NNN % 100 // 10) * 7 + (NNN % 10) * 9) % 11
    if VER_C < 10:
        C = VER_C
    else:
        C = 1

    CNP = (s * 10 ** 12) + (AA * 10 ** 10) + (LL * 10 ** 8) + (ZZ * 10 ** 6) + (jj * 10 ** 4) + (NNN * 10) + C

    return CNP


def Generare_Hash_Key(cnp):
    S = cnp // 10 ** 12
    AA = cnp // 10 ** 10 % 100
    LL = cnp // 10 ** 8 % 100
    ZZ = cnp // 10 ** 6 % 100
    JJ = cnp // 10 ** 4 % 100
    NNN = cnp // 10 % 1000
    C = cnp % 10
    return hash((AA * LL * ZZ * JJ * NNN * C) ** S / 10007) % 1009


def add_values_in_dict(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


def search(key, mydict, lookup):
    for key, value in mydict.items():
        for v in value:
            if lookup in v:
                return v[16:]


if __name__ == '__main__':

    Lista_Cetateni = {}
    lista_CNP = []
    lista_1000_CNP = []

    cnp1 = [6026, 7342, 10732, 10384, 9665, 4817, 6834, 9438, 5711, 7925, 5158, 11711, 11744, 3582, 8836, 11535, 9290,
            5929, 5349, 7469, 4686, 12415, 6594, 8041, 4685, 9325, 8117, 7713, 13310, 5670, 3789, 6627, 10315, 6859,
            11446, 3790, 6629, 6533, 5787, 32037, 5201, 4827]
    cnp2 = [6503, 8293, 11786, 11105, 10693, 5083, 7363, 10404, 6307, 8681, 5685, 12971, 12864, 3825, 9578, 12622, 9941,
            6318, 5637, 8184, 5052, 13126, 7232, 8744, 5064, 10169, 8791, 8324, 14811, 6394, 4181, 7361, 11117, 7489,
            12788, 3971, 6891, 7169, 6332, 39135, 5679, 5303]
    cnp5 = [2395, 3032, 4173, 4815, 4302, 2263, 3324, 3928, 2121, 3071, 2033, 4917, 4922, 1589, 3883, 4588, 3918, 2507,
            2329, 2729, 2046, 6676, 2885, 3691, 1831, 4121, 3457, 3000, 5174, 2646, 1670, 3008, 5330, 2441, 5011, 1509,
            3255, 2512, 2519, 11539, 2302, 2051]
    cnp6 = [2193, 2863, 3930, 4503, 4109, 2148, 3110, 3690, 1921, 2875, 1902, 4955, 4674, 1512, 3639, 4281, 3658, 2325,
            2227, 2545, 1923, 6399, 2725, 3456, 1689, 3926, 3172, 2782, 4849, 2507, 1578, 2869, 4978, 2217, 4931, 1383,
            2999, 2370, 2377, 11459, 2152, 1889]

    selectare_1000_cetateni = 1000

    for i in range(0, 4):
        for j in range(0, 42):
            if i == 0:
                NR_B_A_JUD_j = cnp1[j]
                for c in range(0, NR_B_A_JUD_j):
                    CNP_PERS = Generator_CNP_D(1, j + 1)
                    NUME_PERS = Generator_Nume(1)
                    KEY = Generare_Hash_Key(CNP_PERS)
                    Lista_Cetateni = add_values_in_dict(Lista_Cetateni, KEY, [str(CNP_PERS) + " - " + NUME_PERS])
                    lista_CNP.append(CNP_PERS)
            elif i == 1:
                NR_F_A_JUD_j = cnp2[j]
                for c in range(0, NR_F_A_JUD_j):
                    CNP_PERS = Generator_CNP_D(2, j + 1)
                    NUME_PERS = Generator_Nume(2)
                    KEY = Generare_Hash_Key(CNP_PERS)
                    Lista_Cetateni = add_values_in_dict(Lista_Cetateni, KEY, [str(CNP_PERS) + " - " + NUME_PERS])
                    lista_CNP.append(CNP_PERS)
            elif i == 2:
                NR_B_C_JUD_j = cnp5[j]
                for c in range(0, NR_B_C_JUD_j):
                    CNP_PERS = Generator_CNP_D(5, j + 1)
                    NUME_PERS = Generator_Nume(5)
                    KEY = Generare_Hash_Key(CNP_PERS)
                    Lista_Cetateni = add_values_in_dict(Lista_Cetateni, KEY, [str(CNP_PERS) + " - " + NUME_PERS])
                    lista_CNP.append(CNP_PERS)
            elif i == 3:
                NR_F_C_JUD_j = cnp6[j]
                for c in range(0, NR_F_C_JUD_j):
                    CNP_PERS = Generator_CNP_D(6, j + 1)
                    NUME_PERS = Generator_Nume(6)
                    KEY = Generare_Hash_Key(CNP_PERS)
                    Lista_Cetateni = add_values_in_dict(Lista_Cetateni, KEY, [str(CNP_PERS) + " - " + NUME_PERS])
                    lista_CNP.append(CNP_PERS)

    for i in range(0, 1000):
        lista_1000_CNP.append(lista_CNP[i * selectare_1000_cetateni])

    for i in range(0, 1000):
        V_CNP = lista_1000_CNP[i]
        S = V_CNP // 10 ** 12
        AA = V_CNP // 10 ** 10 % 100
        LL = V_CNP // 10 ** 8 % 100
        ZZ = V_CNP // 10 ** 6 % 100
        JJ = V_CNP // 10 ** 4 % 100
        NNN = V_CNP // 10 % 1000
        C = V_CNP % 10
        key = hash((AA * LL * ZZ * JJ * NNN * C) ** S / 10007) % 1009
        print("Persoana cu codul ", key, "si CNP : ", V_CNP, "  se numeste : ", search(key, Lista_Cetateni, str(V_CNP)))

#    for i in range(0, 9):
#        CNP_PERS = Generator_CNP()
#        NUME_PERS = Generator_Nume(CNP_PERS//10**12)
#        Lista_Cetateni[CNP_PERS] = NUME_PERS
