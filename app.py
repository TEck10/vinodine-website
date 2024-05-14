import streamlit as st
import requests


# URL for VinoDine API
url = 'https://vinodine3-dxr2er4ueq-ew.a.run.app/predict'

# st.image("https://cdn.pixabay.com/photo/2024/05/05/23/00/ai-generated-8742016_1280.jpg", caption='VinoDine', output_format="auto")

st.markdown("""<h4 style='text-align: center; '>Unlock your <b>perfect Wine and Food pairing</b> in just 5 questions!</h4>""", unsafe_allow_html=True)

grapes = ['"BiancodAlessano"', '"LAcadieBlanc"', '"LendelEl"', '"LoindelOeil"', '"NerodAvola"', '"PineauDAunis"', '"RoussetteDAyze"', '"TrebbianodAbruzzo"', 'Abbuoto', 'Abouriou', 'Abrostine', 'Acolon', 'Agiorgitiko', 'Aglianico', 'Aidani', 'Airen', 'Albalonga', 'Albana', 'Albanella', 'Albariño', 'Albarola', 'Albarossa', 'AlbarínBlanco', 'Albillo', 'AlbilloCrimean', 'AlbilloMayor', 'AlbillodeAlbacete', 'Aleatico', 'AlfrocheiroPreto', 'Alibernet', 'AlicanteBouschet', 'AlicanteGanzin', 'Aligoté', 'Altesse', 'Alvarelhão', 'Alvarinho', 'Amigne', 'Ancellotta', 'Ansonica', 'AntãoVaz', 'Aragonez', 'Aramon', 'Arbane', 'Areni', 'Argaman', 'Arinarnoa', 'Arinto', 'ArintodeBucelas', 'ArintodosAçores', 'Arneis', 'Arnsburger', 'Arriloba', 'AspiranBouschet', 'AsprinioBianco', 'AssarioBranco', 'Assyrtiko', 'Athiri', 'Aurore', 'Avanà', 'Avesso', 'Avgoustiatis', 'AzalBranco', 'AzalTinto', 'Babić', 'Bacchus', 'BacoNoir', 'Baga', 'Barbarossa', 'Barbera', 'Barcelo', 'Barsaglina', 'BastardoMagarachsky', 'Batoca', 'Bellone', 'Bianca', 'Biancame', 'BianchettaTrevigiana', 'Biancolella', 'Bical', 'BlackQueen', 'Blauburger', 'Blauburgunder', 'BlauerPortugieser', 'Blaufränkisch', 'BoalBranco', 'Bobal', 'Bogazkere', 'BombinoBianco', 'BombinoNero', 'Bonamico', 'Bonarda', 'Bordô', 'Borraçal', 'Bosco', 'Bourboulenc', 'Bovale', 'Brachetto', 'Braquet', 'Braucol', 'Brianna', 'Bronner', 'BrunArgenté', 'Bruñal', 'Bual', 'BudaiZöld', 'Bukettraube', 'BurgundMare', 'BusuioacadeBohotin', 'BăbeascăNeagră', 'CabernetBlanc', 'CabernetCortis', 'CabernetCubin', 'CabernetDorsa', 'CabernetFranc', 'CabernetJura', 'CabernetMitos', 'CabernetRuby', 'CabernetSauvignon', 'CabernetSeverny', 'Cagnulari', 'CaiñoBlanco', 'CaiñoTinto', 'CalabresediMontenuovo', 'Caladoc', 'Calkarasi', 'Callet', 'Camarate', 'CanaioloBlanco', 'CanaioloNero', 'Cannonau', 'Carignan/Cariñena', 'Carmenère', 'Carricante', 'Casavecchia', 'Cascade', 'Casetta', 'Castelão', 'CatarrattoBianco', 'Catawba', 'CayugaWhite', 'Cencibel', 'Centesiminio', 'CercealBranco', 'Cesanese', 'Chambourcin', 'Chancellor', 'Charbono', 'Chardonel', 'Chardonnay', 'ChardonnayMusqué', 'Chasan', 'Chasselas', 'Chatus', 'Chenanson', 'CheninBlanc', 'Chinuri', 'Cienna', 'Ciliegiolo', 'Cinsault', 'Clairette', 'Cococciola', 'CodadiVolpeBianca', 'Colobel', 'Colombard', 'Coloraillo', 'ColorinodelValdarno', 'Concord', 'CorintoNero', 'Cornalin', 'Cornifesto', 'CorotNoir', 'Cortese', 'Corvina', 'Corvinone', 'Couderc', 'Counoise', 'CriollaGrande', 'Croatina', 'Crouchen', 'Cynthiana', 'CôdegadeLarinho', 'Côt', 'Dafni', 'Dakapo', 'DeChaunac', 'Debina', 'Diagalves', 'Dimiat', 'Dimrit', 'Dindarella', 'Diolinoir', 'Dolcetto', 'Domina', 'DonaBlanca', 'DonzelinhoBranco', 'DonzelinhoTinto', 'Dornfelder', 'Drupeggio', 'Dunkelfelder', 'Duras', 'Durella', 'Durif', 'DzvelshaviObchuri', 'Edelweiss', 'Egiodola', 'Ehrenfelser', 'EmeraldRiesling', 'Emir', 'Enantio', 'Encruzado', 'Erbaluce', 'Espadeiro', 'Falanghina', 'FalanghinaBeneventana', 'Famoso', 'Favorita', 'Fenile', 'FerServadou', 'FernãoPires', 'FeteascaAlba', 'FeteascaNeagra', 'FeteascaRegala', 'Fiano', 'Flora', 'FogliaTonda', 'Fokiano', 'Folgasao', 'FolleBlanche', 'FonteCal', 'Fragolino', 'Francusa', 'Frappato', 'Fredonia', 'Freisa', 'Friulano/Sauvignonasse', 'Frontenac', 'FruhroterVeltliner', 'Frühburgunder', 'Fumin', 'FuméBlanc', 'Furmint', 'Gaglioppo', 'Gaidouria', 'Galotta', 'Gamaret', 'GamayNoir', 'GamayTeinturierdeBouze', 'GambadiPernice', 'Garanoir', 'Garganega', 'Garnacha', 'GarnachaBlanca', 'GarnachaPeluda', 'GarnachaRoja', 'GarnachaTinta', 'GarnachaTintorera', 'GarridoFino', 'GelberMuskateller', 'Gewürztraminer', 'Gigiac', 'Ginestra', 'Girgentina', 'GiròBlanc', 'Glera/Prosecco', 'Godello', 'GoldTraminer', 'Goldburger', 'Golubok', 'Gorgollasa', 'GoruliMtsvane', 'Gouveio', 'GouveioReal', 'Graciano', 'GrandNoir', 'GrasadeCotnari', 'Grauburgunder', 'Grecanico', 'Grechetto', 'GrechettoRosso', 'Greco', 'GrecoBianco', 'GrecoNero', 'Grenache', 'GrenacheBlanc', 'GrenacheGris', 'Grignolino', 'Grillo', 'Gringet', 'Grolleau', 'Groppello', 'GrosManseng', 'GrosVerdot', 'GrünerVeltliner', 'Guardavalle', 'Gutedel', 'Hanepoot', 'Helios', 'Hibernal', 'HondarrabiBeltza', 'HondarrabiZuri', 'HumagneBlanche', 'HumagneRouge', 'Huxelrebe', 'Hárslevelű', 'IncrocioManzoni', 'Inzolia', 'IrsaiOliver', 'Isabella', 'Jacquère', 'Jaen', 'Jampal', 'Johannisberg', 'Johanniter', 'JuanGarcia', 'Kabar', 'Kadarka', 'Kakhet', 'Kakotrygis', 'KalecikKarasi', 'Kangun', 'Karasakiz', 'Karmahyut', 'Katsano', 'Keratsuda', 'Kerner', 'Khikhvi', 'Királyleányka', 'Kisi', 'Klevner', 'KokurBely', 'Koshu', 'Kotsifali', 'KrasnostopAnapsky', 'KrasnostopZolotovsky', 'Kratosija', 'Krstac', 'Kydonitsa', 'Kékfrankos', 'Lacrima', 'Lafnetscha', 'Lagrein', 'Lambrusco', 'Lampia', 'LandotNoir', 'Lauzet', 'Leanyka', 'Lefkada', 'Lemberger', 'Lenoir', 'LeonMillot', 'Liatiko', 'Limnio', 'Limniona', 'ListanNegro', 'Lorena', 'Loureiro', 'Macabeo', 'MadeleineAngevine', 'MaglioccoCanino', 'Malagouzia', 'Malbec', 'MalboGentile', 'Malvar', 'Malvasia', 'MalvasiaBiancaLunga', 'MalvasiaFina', 'MalvasiaIstriana', 'MalvasiaNera', 'MalvasiadelLazio', 'MalvasiadiCandia', 'MalvasiadiLipari', 'MalvasiadiSchierano', 'MalvazijaIstarska', 'Mammolo', 'Mandilaria', 'Mandón', 'Manseng', 'Manteudo', 'MantoNegro', 'ManzoniBianco', 'Maratheftiko', 'MarechalFoch', 'MariaGomes', 'Marmajuelo', 'Marquette', 'Marsanne', 'Marselan', 'Marufo', 'Marzemino', 'Mataro', 'MaturanaBlanca', 'MaturanaTinta', 'MauzacBlanc', 'MauzacNoir', 'Mavro', 'MavroKalavritino', 'Mavrodafni', 'Mavrotragano', 'MavroudiArachovis', 'Mavrud', 'Mayolet', 'Mazuelo', 'Melnik', 'Melody', 'MelondeBourgogne', 'Mencia', 'Menoir', 'Merlot', 'Merseguera', 'Michet', 'Millot-Foch', 'MisketCherven', 'MisketVrachanski', 'ModrýPortugal', 'Molinara', 'Mollard', 'Monastrell', 'MondeuseNoire', 'Monica', 'Montepulciano', 'Montuni', 'Moradella', 'Morava', 'Morellino', 'Morenillo', 'Moreto', 'Morio-Muskat', 'Moristel', 'Moschofilero', 'Moschomavro', 'Mouhtaro', 'Mourisco', 'Mourvedre', 'MtsvaneKakhuri', 'Muscadelle', 'Muscadine', 'Muscardin', 'Muscat/MoscatelGalego', 'Muscat/MoscatelRoxo', 'Muscat/MoscateldeGranoMenudo', 'Muscat/MoscatelloSelvatico', 'Muscat/Moscato', 'Muscat/MoscatoBianco', 'Muscat/MoscatoGiallo', 'Muscat/MoscatoRosa', 'Muscat/MoscatodiScanzo', 'Muscat/Muscatel', 'Muscat/MuskatMoravsky', 'MuscatBaileyA', 'MuscatBlack', 'MuscatBlanc', 'MuscatEarly', 'MuscatGolden', 'MuscatNoir', 'MuscatOrange', 'MuscatOttonel', 'MuscatValvin', 'MuscatYellow', 'MuscatofAlexandria', 'MuscatofFrontignan', 'MuscatofHamburg', 'MuscatofSetúbal', 'MustoasadeMaderat', 'Müller-Thurgau', 'Narince', 'Nascetta', 'Nasco', 'Nebbiolo', 'Negoska', 'NegraraTrentino', 'NegraraVeronese', 'Negrette', 'Negroamaro', 'NegrudeDragasani', 'NerelloCappuccio', 'NerelloMascalese', 'NerettaCuneese', 'NeroBuonodiCori', 'NerodiTroia', 'Neuburger', 'Niagara', 'NiagaraBlanc', 'Nieddera', 'Nielluccio', 'Noble', 'Nocera', 'Noiret', 'Norton', 'Nosiola', 'Nouvelle', 'Nuragus', 'Ojaleshi', 'OlaszRizling', 'Ondenc', 'Orion', 'OrleansGelb', 'Ortega', 'Ortrugo', 'Oseleta', 'OtskhanuriSapere', 'Padeiro', 'Pagadebit', 'Palava', 'PallagrelloBianco', 'PallagrelloNero', 'Palomino', 'Pamid', 'Pampanuto', 'Parellada', 'Parraleta', 'Pascale', 'Passerina', 'Pavana', 'País/Mission', 'Pecorino', 'Pederna', 'Pedral', 'PedroXimenez', 'Pelaverga', 'Peloursin', 'Perera', 'Perle', 'Perricone', 'Perrum', 'PetitCourbu', 'PetitManseng', 'PetitMeslier', 'PetitRouge', 'PetitVerdot', 'PetiteArvine', 'PetiteMilo', 'PetitePearl', 'PetiteSirah', 'Peverella', 'Phoenix', 'Picardan', 'PiccolaNera', 'Picolit', 'PicpoulBlanc', 'Piedirosso', 'Pigato', 'Pignoletto', 'Pignolo', 'Pinenc', 'PinotAuxerrois', 'PinotBlanc', 'PinotGrigio', 'PinotGris', 'PinotMeunier', 'PinotNero', 'PinotNoir', 'Pinotage', 'PiquepoulBlanc', 'PiquepoulNoir', 'PlavacMali', 'PolleraNera', 'PosipBijeli', 'Poulsard', 'Premetta', 'Prensal', 'PretoMartinho', 'PrietoPicudo', 'Primitivo', 'Prié', 'Procanico', 'Prokupac', 'PrugnoloGentile', 'Pugnitello', 'Pulcinculo', 'Rabigato', 'RabodeOvelha', 'RabosoPiave', 'RabosoVeronese', 'Ramisco', 'Rebo', 'Refosco', 'RefoscodalPeduncoloRosso', 'Regent', 'Reichensteiner', 'RibollaGialla', 'Riesel', 'Rieslaner', 'Riesling', 'RieslingItálico', 'RieslingRenano', 'Ripolo', 'Rivaner', 'Rkatsiteli', 'Robola', 'Roditis', 'Roesler', 'Rolle/Rollo', 'Romeiko', 'Romé', 'Rondinella', 'Rondo', 'Roobernet', 'Roscetto', 'Rosetta', 'Rossese', 'Rossignola', 'Rossola', 'Rotberger', 'RoterVeltliner', 'Rotgipfler', 'Rougeon', 'Roupeiro', 'Roussanne', 'RoyaldeAlloza', 'Rubin', 'Rubired', 'Ruché', 'Ruen', 'Rufete', 'Ruggine', 'Ruländer', 'Räuschling', 'Sabrevois', 'Sacy', 'Sagrantino', 'Samsó', 'Sangiovese', 'Saperavi', 'Sarba', 'SauvignonBlanc', 'SauvignonGris', 'SavagninBlanc', 'Savatiano', 'Scheurebe', 'Schiava', 'SchiavaGentile', 'SchiavaGrigia', 'Schioppettino', 'Schwarzriesling', 'Schönburger', 'Sciacarello', 'Sciascinoso', 'SearaNova', 'Segalin', 'Seibel', 'Sercial', 'Sercialinho', 'SeyvalBlanc', 'ShirokaMelnishka', 'Sibirkovi', 'Sideritis', 'Siegerrebe', 'Silvaner/Sylvaner', 'Smederevka', 'Solaris', 'Sousão', 'SouvignierGris', 'Spätburgunder', 'St.Croix', 'St.Laurent', 'Steuben', 'Sultana', 'Sultaniye', 'Sumoll', 'SumollBlanc', 'Susumaniello', 'SwensonWhite', 'Symphony', 'Syrah/Shiraz', 'Syriki', 'Szürkebarát', 'Sémillon', 'Síria', 'TamaioasaRomaneasca', 'Tamarez', 'Tannat', 'Tarrango', 'Tazzelenghe', 'Tempranillo', 'TempranilloBlanco', 'Teroldego', 'Terrano', 'Terrantez', 'Terret', 'Thrapsathiri', 'Tibouren', 'Timorasso', 'TintaAmarela', 'TintaBarroca', 'TintaCaiada', 'TintaCarvalha', 'TintaFrancisca', 'TintaMadeira', 'TintaMiúda', 'TintaNegraMole', 'TintaRoriz', 'TintadeToro', 'TintadelPais', 'Tintilia', 'Tintilla', 'TintoCão', 'TintoFino', 'TintoreDiTramonti', 'TocaiFriulano', 'TocaiItalico', 'Torbato', 'Torrontés', 'TourigaFranca', 'TourigaNacional', 'Trajadura', 'Traminer', 'Traminette', 'Trebbiano', 'TrebbianoGiallo', 'TrebbianoRomagnolo', 'TrebbianoToscano', 'Treixadura', 'Trepat', 'Trincadeira', 'Triomphe', 'Trollinger', 'Trousseau', 'TsimlyanskyCherny', 'Tsolikouri', 'Turan', 'Turbiana', 'UghettadiCanneto', 'UgniBlanc', 'UlldeLlebre', 'UvaRara', 'Vaccareze', 'Valdiguie', 'ValentinoNero', 'Verdeca', 'Verdejo', 'Verdelho', 'Verdello', 'Verdicchio', 'Verdiso', 'VerduzzoFriulano', 'Vermentino', 'VermentinoNero', 'Vernaccia', 'VernacciadiOristano', 'VernacciadiSanGimignano', 'Vernatsch', 'Vespaiola', 'Vespolina', 'VidalBlanc', 'Vidiano', 'ViendeNus', 'Vignoles', 'Vijiriega', 'Vilana', 'VillardNoir', 'Vincent', 'Vinhão', 'Viognier', 'Violeta', 'Viorica', 'Viosinho', 'Vital', 'Vitovska', 'Viura', 'Vranac', 'Weissburgunder', 'Welschriesling', 'Xarel-lo', 'Xinomavro', 'Xynisteri', 'Zalema', 'Zelen', 'Zengö', 'Zibibbo', 'Zierfandler', 'Zinfandel', 'ZinfandelWhite', 'Zlahtina', 'Zweigelt', 'Zéta', 'ÁguaSanta', 'Öküzgözü']
st.write('Select the type of wine')
Type  = st.selectbox('Type of the wine', options=['Red', 'White', 'Rose', 'Sparkling', 'Dessert/Port', 'Dessert'],
                     placeholder='Choose the type of wine...', index=None, label_visibility='collapsed')

st.write('Select the body of wine')
Body  = st.selectbox('Body of the wine', options=['Very full-bodied','Full-bodied', 'Medium-bodied', 'Light-bodied','Very light-bodied'],
                     placeholder='Choose the body of the wine...', index=None, label_visibility='collapsed')

st.write('Select the acidicity of the wine')
Acidity = st.selectbox("acidity of  wine", options=['High', 'Medium', 'Low'],
                       placeholder='Choose the acidity of the wine...', index=None, label_visibility='collapsed')

st.write('Select at least of type of grapes')
Grapes = st.multiselect("Type of grapes", options=grapes,
                        placeholder='Select the type of the grapes...', label_visibility='collapsed')

if Grapes == ['']:
    st.write("Please choose at least one sort of grapes")

st.write("Provide the alcohol percentage (in %)")
ABV = st.text_input("alcohol percentage", value=12.0, label_visibility='collapsed')
if "," in ABV:
    ABV=ABV.replace(",",".")

if st.button('Results'):
    if Type == '' or Body == '' or Acidity == '' or len(Grapes) == 0 or ABV == '':
        st.error('Please answer all questions to proceed')
    else:
        params = {'Type': Type,
            'ABV': float(ABV),
            'Body': Body,
            'Acidity': Acidity,
            'grapes': Grapes}

        # st.write(params)
        response = requests.get(url, params=params).json()['foods']
        # st.write(response)

        '''
        ### Suggested foods:
        '''
        i = 1
        for food in response:
            st.write(f'{i}. {food}')
            i += 1

def run():
    st.markdown("<h4 style='text-align: center; '>The creators of VinoDine</h4>", unsafe_allow_html=True)
    image_size = 120

    # https://kitt.lewagon.com/camps/414/contracts
    # document.querySelectorAll('tr').forEach(elt => {
    #     const img = elt.getElementsByTagName('img');
    #     if (img.length > 0) {
    #         const name = elt.getElementsByTagName('td')[1].innerText;
    #         const src = img[0].src;
    #         console.log(`'${name}' : '${src}',`);
    #     }
    # });

    CREATORS = {
        'Arjan' : 'https://avatars.githubusercontent.com/u/161768796?v=4',
        'Florian' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710834888/uzueseo7zyyykjantnnn.jpg',
        'James' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710833790/s6zy2sc8qsmrlf0g04ac.jpg',
        'Tobias' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710264098/h5jfyf2dqi2lor5zdbc5.jpg'
    }

    CREATOR_CSS = f"""
    #creators {{
        display: flex;
        flex-wrap: wrap;
    }}

    .creator-card {{
        display: flex;
        flex-direction: column;
    }}

    .creator-card img {{
        width: {image_size}px;
        height: {image_size}px;
        border-radius: 100%;
        padding: 5px;
        margin: 20px;
        margin-left: 35px;
        box-shadow: 0 0 4px #eee;
    }}

    .creator-card span {{
        text-align: center;
    }}
    """


    CREATOR_CARD = """\
        <div class="creator-card">
            <img src="{url}">
            <span>{name}</span>
        </div>
    """

    creators = ''.join([CREATOR_CARD.format(name=f'{name.split()[0]}', url=url) for name, url in CREATORS.items()])

    CREATOR_HTML = f"""
    <style>
    {CREATOR_CSS}
    </style>
    <div id="creators">
        {creators}
    </div>
    """

    st.write(CREATOR_HTML, unsafe_allow_html=True)

run()

background_style = """
.stApp {
  background-image: url(https://cdn.pixabay.com/photo/2019/03/23/23/38/wine-4076627_1280.jpg);
  background-size: cover;
  opacity:1
}
"""

st.markdown(f'<style>{background_style}</style>', unsafe_allow_html=True)
