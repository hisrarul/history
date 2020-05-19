package Test;

import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;


import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class App {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\israrul\\Downloads\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.get("https://intellipaat.com/");
		driver.manage().window().maximize();
		
		driver.findElement(By.className("main-search")).sendKeys("DevOps");
		driver.findElement(By.id("frontpagesubmitsearch")).click();
		driver.manage().timeouts().implicitlyWait(3,TimeUnit.SECONDS);
		
		String firstData = driver.findElement(By.className("block_title")).getText();
		String CheckData = "DevOps Certification Training Course";
				
		if(firstData.equals(CheckData)) {
			driver.findElement(By.className("block_media")).click();
			driver.manage().timeouts().implicitlyWait(3,TimeUnit.SECONDS);
		}
		else {
			System.out.println("Course not found!");
		}

		String actualData = driver.findElement(By.className("title")).getText();
		String expectedData = "DevOps Certification Training Course";
				
		if(actualData.equals(expectedData)) {
			System.out.println("Found String!");			
			String dateView = driver.findElement(By.className("batchDate")).getText();
			String timeView = driver.findElement(By.className("batchWeek")).getText();
			System.out.println("Next Batch is on: \n"+ dateView + "\n"+ timeView);
			System.out.println("Test Successful");
			driver.close();	
		}
		else {
			System.out.println("Oops!! String Not Found.");
		}

		
	}

}
