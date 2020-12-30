package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class CategoriaDAO {

    public Categoria doRetrieveCategoriaByNome(String nome) {

        try (Connection con = ConPool.getConnection()) {

            PreparedStatement ps = con.prepareStatement("select * from categoria where nome = ?");

            ps.setString(1, nome);
            ResultSet rs = ps.executeQuery();

            Categoria c = new Categoria();

            while (rs.next()) {

                c.setNome(rs.getString(1));
                c.setCane(rs.getString(2));
                c.setAuto(rs.getString(3));
                c.setQuadro(rs.getString(4));
                c.setSoleggiato(rs.getString(5));
                c.setGatto(rs.getString(6));
                c.setMoto(rs.getString(7));
                c.setScultura(rs.getString(8));
                c.setCoperto(rs.getString(9));
            }

            return c;

        } catch (SQLException e) {

            throw new RuntimeException(e);
        }
    }
}
