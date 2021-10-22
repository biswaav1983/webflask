//stage 'Build'

node ('Ubuntu-app-agent'){
def app
try {
    notifyBuild('STARTED')
    
    stage('Cloning Git') {
        /* Let's make sure we have the repository cloned to our workspace */
    checkout scm
		}
    
    stage('Build-and-Tag') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("avisdocker/helloflask:new")
		}

    stage('Post-to-dockerhub') {

     docker.withRegistry('https://registry.hub.docker.com', 'dockerflask') {
     app.push("latest")
        			}
         }
		
    stage('Pull-image-server') {

        sh "docker-compose down"
        sh "docker-compose up -d"
		}

	/* ... existing build steps ... */

   } 

   catch (e) {

     // If there was an exception thrown, the build failed

     currentBuild.result = "FAILED"

     throw e

   } finally {

     // Success or failure, always send notifications

     notifyBuild(currentBuild.result)

   }

 }

 def notifyBuild(String buildStatus = 'STARTED') {

   // build status of null means successful

   buildStatus =  buildStatus ?: 'SUCCESSFUL'

   // Default values



   def subject = "${buildStatus}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'"

   def summary = "${subject} (${env.BUILD_URL})"

   def details = """<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
     <p>Check console output at "<a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>"</p>"""


   // Send notifications

   emailext (

       subject: subject,
       body: details,
	   mimeType: 'text/html',

      // recipientProviders: [[$class: 'DevelopersRecipientProvider']]
	   to: 'avispiku@gmail.com'

     )

 }
