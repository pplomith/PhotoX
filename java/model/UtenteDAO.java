package model;

import java.sql.*;

public class UtenteDAO {

    public UtenteDAO() { }

    public void registraUtente(Utente u) {

        try (Connection con = ConPool.getConnection()) {

            PreparedStatement ps = con.prepareStatement("insert into utente (username, passwordUtente, categoria) " +
                    "values (?, ?, ?)");

            ps.setString(1, u.getUsername());
            ps.setString(2, u.getPassword());
            ps.setString(3, u.getCategoria());

            if (ps.executeUpdate() != 1)
                throw new RuntimeException("insert error!");

        } catch(SQLException e) {

            throw new RuntimeException(e);
        }
    }
}
