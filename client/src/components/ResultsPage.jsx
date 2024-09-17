import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './ResultsPage.css'; // Importing the CSS file

export const ResultsPage = () => {
    const { resultId, query } = useParams();
    const [results, setResults] = useState([]);

    useEffect(() => {
        const fetchResults = async () => {
            try {
                const response = await fetch(`/results/${resultId}/${query}/`);
                const data = await response.json();
                setResults(data);
            } catch (error) {
                console.log('Error fetching results: ', error);
            }
        };

        fetchResults();
    }, [resultId, query]);

    return (
        <div className="results-container">
            <h1>Results Page</h1>
            <div className="results-list">
                {results.length === 0 ? (
                    <p>No results found for your query.</p>
                ) : (
                    results.map((result) => (
                        <div key={result.id} className="result-item">
                            <div className="result-id">
                                <strong>ID:</strong> {result.id}
                            </div>
                            <div className="result-content">
                                <strong>Content:</strong>
                                {result.lines && result.lines.length > 0 ? (
                                    <ul>
                                        {result.lines.map((line, index) => (
                                            <li key={index} className="result-line">
                                                {line}
                                            </li>
                                        ))}
                                    </ul>
                                ) : (
                                    <p>No lines to display.</p>
                                )}
                            </div>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default ResultsPage;
