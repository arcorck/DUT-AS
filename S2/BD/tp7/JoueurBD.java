import java.sql.*;
import java.util.ArrayList;

public class JoueurBD {
	ConnexionMySQL laConnexion;
	JoueurBD(ConnexionMySQL laConnexion){
		this.laConnexion=laConnexion;
	}

	int maxNumJoueur() throws SQLException{
		return -1;
	}


	int insererJoueur( Joueur j) throws  SQLException{
		return -1;
	}


	void effacerJoueur(int num) throws SQLException {
	}

    void majJoueur(Joueur j)throws SQLException{
    }

    Joueur rechercherJoueurParNum(int num)throws SQLException{
	return null;
    }

    ArrayList<Joueur> listeDesJoueurs() throws SQLException{
	return null;
    }

    String rapportMessage() throws SQLException{
        return "A faire";
    }
}
