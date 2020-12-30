package model;

public class Categoria {

    private String nome;
    private String cane;
    private String auto;
    private String quadro;
    private String soleggiato;
    private String gatto;
    private String moto;
    private String scultura;
    private String coperto;

    public Categoria() { }

    public Categoria(String nome, String cane, String auto, String quadro, String soleggiato, String gatto,
                     String moto, String scultura, String coperto) {

        this.nome = nome;
        this.cane = cane;
        this.auto = auto;
        this.quadro = quadro;
        this.soleggiato = soleggiato;
        this.gatto = gatto;
        this.moto = moto;
        this.scultura = scultura;
        this.coperto = coperto;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCane() {
        return cane;
    }

    public void setCane(String cane) {
        this.cane = cane;
    }

    public String getAuto() {
        return auto;
    }

    public void setAuto(String auto) {
        this.auto = auto;
    }

    public String getQuadro() {
        return quadro;
    }

    public void setQuadro(String quadro) {
        this.quadro = quadro;
    }

    public String getSoleggiato() {
        return soleggiato;
    }

    public void setSoleggiato(String soleggiato) {
        this.soleggiato = soleggiato;
    }

    public String getGatto() {
        return gatto;
    }

    public void setGatto(String gatto) {
        this.gatto = gatto;
    }

    public String getMoto() {
        return moto;
    }

    public void setMoto(String moto) {
        this.moto = moto;
    }

    public String getScultura() {
        return scultura;
    }

    public void setScultura(String scultura) {
        this.scultura = scultura;
    }

    public String getCoperto() {
        return coperto;
    }

    public void setCoperto(String coperto) {
        this.coperto = coperto;
    }

    @Override
    public String toString() {
        return "Categoria{" +
                "nome='" + nome + '\'' +
                ", cane='" + cane + '\'' +
                ", auto='" + auto + '\'' +
                ", quadro='" + quadro + '\'' +
                ", soleggiato='" + soleggiato + '\'' +
                ", gatto='" + gatto + '\'' +
                ", moto='" + moto + '\'' +
                ", scultura='" + scultura + '\'' +
                ", coperto='" + coperto + '\'' +
                '}';
    }
}
