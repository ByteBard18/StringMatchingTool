import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Form from './components/Form';
import ResultsPage from './components/ResultsPage';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/upload" element={<Form />} />
                <Route path="/results/:resultId/:query" element={<ResultsPage />} />
                {/* Add more routes here as needed */}
            </Routes>
        </Router>
    );
};

export default App;
