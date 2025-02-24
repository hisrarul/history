import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.JSONObject;

public class VaultTokenGeneratorForWin {
    public static void main(String[] args) {
        try {
            // Vault address and endpoint
            String vaultAddress = System.getenv("VAULT_ADDR"); // Replace with your Vault address
            String endpoint = "/v1/auth/approle/login";

            // Role ID and Secret ID
            String roleId = System.getenv("VAULT_ROLE_ID"); // Replace with your role_id
            String secretId = System.getenv("VAULT_SECRET_ID"); // Replace with your secret_id
            String namespace = System.getenv("VAULT_NAMESPACE"); // Replace with your secret_id

            // JSON payload
            String jsonInputString = String.format("{\"role_id\": \"%s\", \"secret_id\": \"%s\"}", roleId, secretId);

            // Create URL object
            URL url = new URL(vaultAddress + endpoint);
            HttpURLConnection con = (HttpURLConnection) url.openConnection();

            // Set request method to POST
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json; utf-8");
            con.setRequestProperty("Accept", "application/json");

            // If you need to set a namespace header
            con.setRequestProperty("X-Vault-Namespace", namespace); // Replace with your namespace

            // Enable input and output streams
            con.setDoOutput(true);

            // Write JSON input string to the output stream
            try (OutputStream os = con.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            // Read the response
            try (BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream(), "utf-8"))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
            	// Parse the JSON response
            	JSONObject jsonResponse = new JSONObject(response.toString());
            	String clientToken = jsonResponse.getJSONObject("auth").getString("client_token");

            	System.out.println("Client Token: " + clientToken);
		        setEnvironmentVariable("TEST_VAULT_TOKEN", clientToken);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    private static void setEnvironmentVariable(String key, String value) {
        try {
            ProcessBuilder pb = new ProcessBuilder("cmd.exe", "/c", "setx " + key + " \"" + value + "\" /M");
            pb.inheritIO().start().waitFor();
            System.out.println("Environment variable " + key + " updated successfully.");
        } catch (Exception e) {
            System.out.println("Failed to update environment variable: " + e.getMessage());
        }
    }
}
