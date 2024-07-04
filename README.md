# Voice-Gen - Explore the background of your voice!

##Inspiration
Voice-Gen was created to explore how vocal characteristics can reveal aspects of an individual's ethnic background, providing a unique tool for understanding the relationship between voical and identity. Recognizing the potential for AI to delve into the nuances of speech, I aimed to develop a platform that could offer insights into how ethnicity influences voice characteristics. This project leverages advanced AI techniques and Mel-frequency cepstral coefficients (MFCCs) to analyze and classify voice recordings, facilitating research and applications in linguistics, sociology, and beyond.

##What it does 
Voice-Gen is a sophisticated platform designed to determine the ethnic background of speakers based on their voice recordings. By extracting MFCCs, a key feature in speech processing, the platform accurately classifies recordings using a Gaussian Naive Bayes model. It provides users with insights into how voice characteristics correlate with ethnic identity, offering valuable data for academic research, diversity studies, and personalized user experiences.

##How we built it 
Voice-Gen employs a comprehensive AI-driven approach to analyze and classify voice recordings. The platform uses MFCCs to extract essential features from audio data, which are then fed into a Gaussian Naive Bayes model, trained on thousands of recordings. This model, developed with Pandas, achieves a remarkable test accuracy of 99.13%. Flask is used to create REST API endpoints, allowing seamless data exchange between the frontend and backend. The frontend, built with React and JavaScript, provides a user-friendly interface for uploading and analyzing voice recordings.

##Accomplishments that we're proud of
- Achieving a 99.13% test accuracy in classifying the ethnic background of speakers using voice recordings.
- Successfully integrating AI models and MFCCs for accurate and insightful voice analysis.
- Developing a robust REST API with Flask to facilitate efficient data exchange and processing.
- Creating a user-friendly interface that simplifies the complex process of voice analysis for end-users.

##What's next for Voice-Gen
- Enhancing the AI models to further improve classification accuracy and expand the range of analyzed voice features.
- Extending the platform to include a broader database of voice recordings from diverse ethnic backgrounds.
- Conducting user feedback sessions to refine the platform's usability and relevance in various fields.

##Built With
- **React**: For building the interactive frontend.
- **JavaScript**: To add dynamic features to the web application.
- **HTML5**: For structuring the web content.
- **TailwindCSS**: For add visually pleasing styling to the frontend.
- **Flask**: To create and manage the REST API for backend services.
- **Pandas**: For data processing and implementing the Gaussian Naive Bayes model.
- **Mel-frequency cepstral coefficients (MFCCs)**: For feature extraction from audio recordings.
- **Python**: For developing the backend and machine learning components.
- **AI Techniques**: For building and training the voice classification model.

##Try it out 
To experience Voice-Gen, cd into the backend and use `flask predict.py`, then cd into the frontend and use `npm run dev` on `localhost:3000`. Upload your voice recordings and explore how your voice characteristics relate to ethnic identity today!
