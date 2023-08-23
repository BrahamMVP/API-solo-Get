from fastapi import FastAPI
app = FastAPI()
Libros = [
{"nombre": "Poema de Gilgamesh", "autor": "Anónimo", "idioma": "Acadio"},
{"nombre": "Libro de Job (de la Biblia)", "autor": "Anónimo", "idioma": "Hebreo"},
{"nombre": "Las mil y una noches", "autor": "Anónimo", "idioma": "Árabe"},
{"nombre": "Saga de Njál", "autor": "Anónimo", "idioma": "Nórdico antiguo"},
{"nombre": "Todo se desmorona", "autor": "Achebe, ChinuaChinua Achebe", "idioma": "Inglés"},
{"nombre": "Cuentos infantiles", "autor": "Andersen, Hans ChristianHans Christian Andersen", "idioma": "Danés"},
{"nombre": "Divina comedia", "autor": "Alighieri, DanteDante Alighieri", "idioma": "Italiano"},
{"nombre": "Orgullo y prejuicio", "autor": "Austen, JaneJane Austen", "idioma": "Inglés"},
{"nombre": "Papá Goriot", "autor": "de Balzac, HonoréHonoré de Balzac", "idioma": "Francés"},
{"nombre": "Molloy, Malone muere, El Innombrable, una trilogía", "autor": "Beckett, SamuelSamuel Beckett", "idioma": "Francés, Inglés"},
{"nombre": "Decamerón", "autor": "Boccaccio, GiovanniGiovanni Boccaccio", "idioma": "Italiano"},
{"nombre": "Ficciones", "autor": "Borges, Jorge LuisJorge Luis Borges", "idioma": "Español"},
{"nombre": "Cumbres Borrascosas", "autor": "Brontë, EmilyEmily Brontë", "idioma": "Inglés"},
{"nombre": "El extranjero", "autor": "Camus, AlbertAlbert Camus", "idioma": "Francés"},
{"nombre": "Poemas", "autor": "Leopardi, GiacomoGiacomo Leopardi", "idioma": "Italiano"},
{"nombre": "Viaje al fin de la noche", "autor": "Céline, Louis-FerdinandLouis-Ferdinand Céline", "idioma": "Francés"},
{"nombre": "Don Quijote de la Mancha", "autor": "Cervantes, Miguel deMiguel de Cervantes", "idioma": "Español"},
{"nombre": "Los cuentos de Canterbury", "autor": "Chaucer, GeoffreyGeoffrey Chaucer", "idioma": "Inglés"},
{"nombre": "Relatos cortos", "autor": "Kafka, FranzFranz Kafka", "idioma": "Alemán"},
{"nombre": "Nostromo", "autor": "Conrad, JosephJoseph Conrad", "idioma": "Inglés"},
{"nombre": "Grandes Esperanzas", "autor": "Dickens, CharlesCharles Dickens", "idioma": "Inglés"},
{"nombre": "Jacques el fatalista", "autor": "Diderot, DenisDenis Diderot", "idioma": "Francés"},
{"nombre": "Berlin Alexanderplatz", "autor": "Döblin, AlfredAlfred Döblin", "idioma": "Alemán"},
{"nombre": "Crimen y castigo", "autor": "Dostoievski, FiódorFiódor Dostoievski", "idioma": "Ruso"},
{"nombre": "El idiota", "autor": "Dostoievski, FiódorFiódor Dostoievski", "idioma": "Ruso"},
{"nombre": "Los endemoniados", "autor": "Dostoievski, FiódorFiódor Dostoievski", "idioma": "Ruso"},
{"nombre": "Los hermanos Karamazov", "autor": "Dostoievski, FiódorFiódor Dostoievski", "idioma": "Ruso"},
{"nombre": "Middlemarch", "autor": "Eliot, GeorgeGeorge Eliot", "idioma": "Inglés"},
{"nombre": "El hombre invisible", "autor": "Ellison, RalphRalph Ellison", "idioma": "Inglés"},
{"nombre": "Medea", "autor": "Eurípides", "idioma": "Griego clásico"},
{"nombre": "¡Absalom, Absalom!", "autor": "Faulkner, WilliamWilliam Faulkner", "idioma": "Inglés"},
{"nombre": "El ruido y la furia", "autor": "Faulkner, WilliamWilliam Faulkner", "idioma": "Inglés"},
{"nombre": "Madame Bovary", "autor": "Flaubert, GustaveGustave Flaubert", "idioma": "Francés"},
{"nombre": "La educación sentimental", "autor": "Flaubert, GustaveGustave Flaubert", "idioma": "Francés"},
{"nombre": "Romancero gitano", "autor": "Lorca, Federico GarcíaFederico García Lorca", "idioma": "Español"},
{"nombre": "Cien años de soledad", "autor": "Márquez, Gabriel GarcíaGabriel García Márquez", "idioma": "Español"},
{"nombre": "El amor en los tiempos del cólera", "autor": "Márquez, Gabriel GarcíaGabriel García Márquez", "idioma": "Español"},
{"nombre": "Fausto", "autor": "Goethe, Johann Wolfgang vonJohann Wolfgang von Goethe", "idioma": "Alemán"},
{"nombre": "Almas muertas", "autor": "Gogol, NikolaiNikolai Gogol", "idioma": "Ruso"},
{"nombre": "El tambor de hojalata", "autor": "Grass, GünterGünter Grass", "idioma": "Alemán"},
{"nombre": "Gran Sertón: Veredas", "autor": "Guimarães Rosa, JoãoJoão Guimarães Rosa", "idioma": "Portugués"},
{"nombre": "Hambre", "autor": "Hamsun, KnutKnut Hamsun", "idioma": "Noruego"},
{"nombre": "El viejo y el mar", "autor": "Hemingway, ErnestErnest Hemingway", "idioma": "Inglés"},
{"nombre": "Ilíada", "autor": "Homero", "idioma": "Griego antiguo"},
{"nombre": "Odisea", "autor": "Homero", "idioma": "Griego antiguo"},
{"nombre": "Casa de muñecas", "autor": "Ibsen, HenrikHenrik Ibsen", "idioma": "Noruego"},
{"nombre": "Ulises", "autor": "Joyce, JamesJames Joyce", "idioma": "Inglés"},
{"nombre": "El proceso", "autor": "Kafka, FranzFranz Kafka", "idioma": "Alemán"},
{"nombre": "El castillo", "autor": "Kafka, FranzFranz Kafka", "idioma": "Alemán"},
{"nombre": "Shakuntala", "autor": "Kālidāsa", "idioma": "Sánscrito"},
{"nombre": "El sonido de la montaña", "autor": "Kawabata, YasunariYasunari Kawabata", "idioma": "Japonés"},
{"nombre": "Zorba, el griego", "autor": "Kazantzakis, NikosNikos Kazantzakis", "idioma": "Griego moderno"},
{"nombre": "Hijos y amantes", "autor": "Lawrence, D. H.D. H. Lawrence", "idioma": "Inglés"},
{"nombre": "Gente independiente", "autor": "Laxness, HalldórHalldór Laxness", "idioma": "Islandés"},
{"nombre": "El cuaderno dorado", "autor": "Lessing, DorisDoris Lessing", "idioma": "Inglés"},
{"nombre": "Pippi Calzaslargas", "autor": "Lindgren, AstridAstrid Lindgren", "idioma": "Sueco"},
{"nombre": "Diario de un loco", "autor": "Xun, LuLu Xun", "idioma": "Chino"},
{"nombre": "Hijos de nuestro barrio", "autor": "Mahfuz, NaguibNaguib Mahfuz", "idioma": "Árabe"},
{"nombre": "Los Buddenbrook", "autor": "Mann, ThomasThomas Mann", "idioma": "Alemán"},
{"nombre": "La montaña mágica", "autor": "Mann, ThomasThomas Mann", "idioma": "Alemán"},
{"nombre": "Moby-Dick", "autor": "Melville, HermanHerman Melville", "idioma": "Inglés"},
{"nombre": "Ensayos", "autor": "Montaigne, Michel deMichel de Montaigne", "idioma": "Francés"},
{"nombre": "La historia", "autor": "Morante, ElsaElsa Morante", "idioma": "Italiano"},
{"nombre": "Beloved", "autor": "Morrison, ToniToni Morrison", "idioma": "Inglés"},
{"nombre": "Genji Monogatari", "autor": "Shikibu, MurasakiMurasaki Shikibu", "idioma": "Japonés"},
{"nombre": "El hombre sin atributos", "autor": "Musil, RobertRobert Musil", "idioma": "Alemán"},
{"nombre": "Lolita", "autor": "Nabokov, VladimirVladimir Nabokov", "idioma": "Inglés"},
{"nombre": "1984", "autor": "Orwell, GeorgeGeorge Orwell", "idioma": "Inglés"},
{"nombre": "Las metamorfosis", "autor": "Ovidio", "idioma": "Latín clásico"},
{"nombre": "Libro del desasosiego", "autor": "Pessoa, FernandoFernando Pessoa", "idioma": "Portugués"},
{"nombre": "Cuentos", "autor": "Poe, Edgar AllanEdgar Allan Poe", "idioma": "Inglés"},
{"nombre": "En busca del tiempo perdido", "autor": "Proust, MarcelMarcel Proust", "idioma": "Francés"},
{"nombre": "Gargantúa y Pantagruel", "autor": "Rabelais, FrançoisFrançois Rabelais", "idioma": "Francés"},
{"nombre": "Pedro Páramo", "autor": "Rulfo, JuanJuan Rulfo", "idioma": "Español"},
{"nombre": "Masnavi", "autor": "Rumi", "idioma": "Persa"},
{"nombre": "Hijos de la medianoche", "autor": "Rushdie, SalmanSalman Rushdie", "idioma": "Inglés"},
{"nombre": "Bostan", "autor": "Saadi", "idioma": "persa"},
{"nombre": "Tiempo de migrar al norte", "autor": "Salih, TayebTayeb Salih", "idioma": "Árabe"},
{"nombre": "Ensayo sobre la ceguera", "autor": "Saramago, JoséJosé Saramago", "idioma": "Portugués"},
{"nombre": "Hamlet", "autor": "Shakespeare, WilliamWilliam Shakespeare", "idioma": "Inglés"},
{"nombre": "El rey Lear", "autor": "Shakespeare, WilliamWilliam Shakespeare", "idioma": "Inglés"},
{"nombre": "Otelo", "autor": "Shakespeare, WilliamWilliam Shakespeare", "idioma": "Inglés"},
{"nombre": "Edipo rey", "autor": "Sófocles", "idioma": "Griego clásico"},
{"nombre": "Rojo y negro", "autor": "Stendhal", "idioma": "Francés"},
{"nombre": "Vida y opiniones del caballero Tristram Shandy", "autor": "Sterne, LaurenceLaurence Sterne", "idioma": "Inglés"},
{"nombre": "La conciencia de Zeno", "autor": "Svevo, ItaloItalo Svevo", "idioma": "Italiano"},
{"nombre": "Los viajes de Gulliver", "autor": "Swift, JonathanJonathan Swift", "idioma": "Inglés"},
{"nombre": "Guerra y paz", "autor": "Tolstói, LevLev Tolstói", "idioma": "Ruso"},
{"nombre": "Ana Karenina", "autor": "Tolstói, LevLev Tolstói", "idioma": "Ruso"},
{"nombre": "La muerte de Iván Ilich", "autor": "Tolstói, LevLev Tolstói", "idioma": "Ruso"},
{"nombre": "Las aventuras de Huckleberry Finn", "autor": "Twain, MarkMark Twain", "idioma": "Inglés"},
{"nombre": "Ramayana", "autor": "Valmiki", "idioma": "Sánscrito"},
{"nombre": "Eneida", "autor": "Virgilio", "idioma": "Latín clásico"},
{"nombre": "Mahabhárata", "autor": "Viasa", "idioma": "Sánscrito"},
{"nombre": "Hojas de hierba", "autor": "Whitman, WaltWalt Whitman", "idioma": "Inglés"},
{"nombre": "La señora Dalloway", "autor": "Woolf, VirginiaVirginia Woolf", "idioma": "Inglés"},
{"nombre": "Al faro", "autor": "Woolf, VirginiaVirginia Woolf", "idioma": "Inglés"},
{"nombre": "Memorias de Adriano", "autor": "Yourcenar, MargueriteMarguerite Yourcenar", "idioma": "Francés"}]





@app.get("/Libros/nombre")
async def nombres():
    return [Libro["nombre"] for Libro in Libros]

@app.get("/Libros/idioma")
async def idiomas():
    return [Libro["idioma"] for Libro in Libros]

@app.get("/Libros/autor")
async def autores():
    return [Libro["nombre"] for Libro in Libros]

@app.get("/Libros/Anónimo")
async def anonimo():
    return [Libro["nombre"] for Libro in Libros if Libro["autor"] == "Anónimo"]

@app.get("/Libros/Kafka")
async def Kafka():
    return [Libro["nombre"] for Libro in Libros if Libro["autor"] == "Kafka, FranzFranz Kafka"]

@app.get("/Libros/Tolstói")
async def Tolstói():
    return [Libro["nombre"] for Libro in Libros if Libro["autor"] == "Tolstói, LevLev Tolstói"]

@app.get("/Libros/Mann")
async def Mann():
    return [Libro["nombre"] for Libro in Libros if Libro["autor"] == "Mann, ThomasThomas Mann"]

@app.get("/Libros/Francés")
async def frances():
    return [Libro["nombre"] for Libro in Libros if Libro["idioma"] == "Francés"]

@app.get("/Libros/Inglés")
async def ingles():
    return [Libro["nombre"] for Libro in Libros if Libro["idioma"] == "Inglés"]

@app.get("/Libros/Nombre-Autor")
async def nombre_autor():
    return [{"nombre": Libros["nombre"], "autor": Libros["autor"]} for Libros in Libros]

@app.get("/Libros/Ingles-Autor")
async def ingles_autor():
    return [{"nombre": Libros["nombre"], "autor": Libros["autor"]} for Libros in Libros if Libros["idioma"] == "Inglés"]

@app.get("/Libros/Frances-Autor")
async def frances_autor():
    return [{"nombre": Libros["nombre"], "autor": Libros["autor"]} for Libros in Libros if Libros["idioma"] == "Francés"]