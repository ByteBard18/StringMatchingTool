import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './ResultsPage.css'; // Importing the CSS file
import HighlightedText from '../utils/HighlightedText';

export const ResultsPage = () => {
    const { resultId, query } = useParams();
    const [results, setResults] = useState([]);

    useEffect(() => {
        const fetchResults = async () => {
            try {
                const response = await fetch(`http://localhost:8000/results/${resultId}/${query}/`);
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
                        result.offset_list && result.lines.length > 0 && (
                            <div key={result.id} className="result-item">
                                <div className="result-id">
                                    <strong>ID:</strong> {result.id}
                                </div>
                                {result.lines.length > 0 && (
                                    <div className="result-content">
                                        <strong>Matches:</strong>
                                        <ul>
                                            {result.lines.map((line, index) => (
                                                <li key={index} className="result-line">
                                                    <HighlightedText line={line} searchTerm={query} />
                                                </li>
                                            ))}
                                        </ul>
                                    </div>
                                )}
                            </div>
                        )
                    ))
                )}
            </div>
        </div>
    );
};

export default ResultsPage;
