package controller;

import model.*;

import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

@WebServlet("/registration")
public class ServletRegistration extends HttpServlet {

    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException{

        doGet(request, response);
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Calcolo della categoria dell'utente
        String categoria = calcoloCategoria(request);

        // Creazione del DAO della categoria ed estrazione dei valori
        CategoriaDAO cd = new CategoriaDAO();
        Categoria c = cd.doRetrieveCategoriaByNome(categoria);

        // Calcolo dei path delle foto 
        List<String> foto = calculatePhotoPaths(c);

        System.out.println("Queste sono le foto iniziali");
        System.out.println(c.getNome());
        foto.forEach((f) -> System.out.println(f));

        List<String> foto1 = modifyPath(foto);
        System.out.println("\nQueste sono le foto nuove");
        foto1.forEach((f) -> System.out.println(f));

        request.setAttribute("foto", foto1);

        // Prelievo delle credenziali dell'utente
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        // Creazione dell'oggetto utente
        Utente u = new Utente();
        u.setUsername(username);
        u.setPassword(password);
        u.setCategoria(categoria);

        // Creazione UtenteDAO e salvataggio dell'utente
        UtenteDAO ud = new UtenteDAO();
        ud.registraUtente(u);

        RequestDispatcher rd = getServletContext().getRequestDispatcher("/WEB-INF/results/photo.jsp");
        rd.forward(request, response);
    }

    public String calcoloCategoria(HttpServletRequest request) {

        int[][] punteggiSezioni = new int[10][4];

        // Riempimento prima sezione

        for (int i = 0; i < sezioni; i++) {
            for (int j = 0; j < caratteri; j++) {
                String parameter = (i + 1) + "_" + (j + 1);
                punteggiSezioni[i][j] = Integer.parseInt(request.getParameter(parameter));
            }
        }

        System.out.println("Questi sono i punteggi");
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 4; j++) {
                if (j == 0)
                    System.out.println();

                System.out.print(punteggiSezioni[i][j]);
            }
        }

        String userPersonality = calcoloMax(punteggiSezioni);
        System.out.println(userPersonality);

        return userPersonality;
    }

    private String calcoloMax(int [][] punteggiSezioni) {

        Random rand = new Random();
        int [] carattere = new int[4];

        // Calcolo della somma sulle colonne
        for (int i = 0; i < sezioni; i++) {
            for (int k = 0; k < caratteri; k++)
                carattere[k] += punteggiSezioni[i][k];
        }

        // Calcolo del massimo
        int max = carattere[0];
        for (int i = 1; i < caratteri; i++) {
            if (max < carattere[i])
                max = carattere[i];
        }


        // Calcolo delle colonne con il massimo
        int i;
        ArrayList<Integer> indici = new ArrayList<>();
        for (i = 0; i < caratteri; i++) {
            if (max == carattere[i]) {
                indici.add(i);
            }
        }

        int n = rand.nextInt(indici.size());

        System.out.println(n);

        return personality[indici.get(n)];
    }

    private List<String> calculatePhotoPaths(Categoria c) {

        // Conversione da valori attesi in valori interi
        // per calcolare il numero di foto di quella categoria su 10
        int cane = (int)(Double.parseDouble(c.getCane()) * 10);
        int auto = (int)(Double.parseDouble(c.getAuto()) * 10);
        int quadro = (int)(Double.parseDouble(c.getQuadro()) * 10);
        int soleggiato = (int)(Double.parseDouble(c.getSoleggiato()) * 10);


        // ArrayList contenente tutte le foto
        List<String> foto = new ArrayList<>();

        // Aggiunta delle foto per ciascuna categoria
        fotoCategoria(foto, cane, pathAnimali, "Cani", "Gatti");
        fotoCategoria(foto, auto, pathVeicoli, "Auto", "Moto");
        fotoCategoria(foto, quadro, pathOpere, "Quadri", "Sculture");
        fotoCategoria(foto, soleggiato, pathTempo, "Soleggiato", "Coperto");

        return foto;
    }

    // Funzione generale che presi i parametri in input
    // returna i nomi delle foto nella cartella
    // dopodichè chiama la funzione inserimentoFoto che inserisce le foto nell'ArrayList foto
    private void fotoCategoria(List<String> foto, int cat1, String pathGeneral,
                               String nomeCat1, String nomeCat2) {

        int cat2 = 10 - cat1;

        String pathCat1 = pathGeneral + nomeCat1 + "Selezione/";
        String pathCat2 = pathGeneral + nomeCat2 + "Selezione/";

        File file = new File(pathCat1);
        String[] fotoCat1 = file.list();

        file = new File(pathCat2);
        String[] fotoCat2 = file.list();

        inserimentoFoto(foto, cat1, cat2, pathCat1, pathCat2, fotoCat1, fotoCat2);
    }

    // Funzione che chiama la funzione ccleFunction
    private void inserimentoFoto(List<String> foto, int cat1, int cat2, String path1,
                            String path2, String[] foto1, String[] foto2) {

        cycleFunction(foto, cat1, path1, foto1);
        cycleFunction(foto, cat2, path2, foto2);
    }

    // Funzione che cicla all'interno l'array delle foto provenienti dalle cartelle
    // e ne seleziona tante quante il limite cat esprime, senza ripetizioni
    private void cycleFunction(List<String> foto, int cat, String pathSpecific, String[] fotoSpecific) {

        Random rand = new Random();

        String path;
        String f;
        for (int i = 0; i < cat;) {

            f = fotoSpecific[rand.nextInt(fotoSpecific.length)];

            if (f.equalsIgnoreCase(".DS_Store")){ }

            else {
                path = pathSpecific + f;
                if (!foto.contains(path)) {
                    foto.add(path);
                    i++;
                }
            }
        }
    }

    private List<String> modifyPath(List<String> foto) {

        List<String> foto1 = new ArrayList<>();

        for (int i = 0; i < foto.size(); i++) {
            String path;
            if (foto.get(i).substring(24, 31).equalsIgnoreCase("Animali")) {
                path = "./image" + foto.get(i).substring(31);
                foto1.add(path);
                System.out.println(path);
            }
            else if (foto.get(i).substring(24, 31).equalsIgnoreCase("Veicoli")) {
                path = "./image" + foto.get(i).substring(31);
                foto1.add(path);
                System.out.println(path);
            }
            else if (foto.get(i).substring(24, 29).equalsIgnoreCase("Opere")) {
                path = "./image" + foto.get(i).substring(29);
                foto1.add(path);
                System.out.println(path);
            }
            else {
                path = "./image" + foto.get(i).substring(29);
                foto1.add(path);
                System.out.println(path);
            }
        }

        return foto1;
    }

    public static final int sezioni = 10;
    public static final int caratteri = 4;
    public static final String[] personality = {"Leone", "Lontra", "Golden Retriever", "Castoro"};
    public static final String pathAnimali = "/Users/memex_99/Desktop/Animali/AnimaliSelezione/";
    public static final String pathVeicoli = "/Users/memex_99/Desktop/Veicoli/VeicoliSelezione/";
    public static final String pathOpere = "/Users/memex_99/Desktop/Opere/OpereSelezione/";
    public static final String pathTempo = "/Users/memex_99/Desktop/Tempo/TempoSelezione/";
}
