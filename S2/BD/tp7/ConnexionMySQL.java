import java.sql.*;

public class ConnexionMySQL {
	private Connection mysql;
	private boolean connecte=false;
	public ConnexionMySQL() throws ClassNotFoundException{
	}

	public void connecter(String nomServeur, String nomBase, String nomLogin, String motDePasse) throws SQLException {
	}
	public void close() throws SQLException {
	}

        public boolean isConnecte(){ return this.connecte;}

        public Blob createBlob()throws SQLException{
		return this.mysql.createBlob();
	}
	public Statement createStatement() throws SQLException {
		return this.mysql.createStatement();
	}

	public PreparedStatement prepareStatement(String requete) throws SQLException{
		return this.mysql.prepareStatement(requete);
	}
	
}
