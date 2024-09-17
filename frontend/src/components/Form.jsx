import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from './Form.module.css'; // Import the CSS module

const Form = () => {
    const [files, setFiles] = useState([]);
    const [query, setQuery] = useState('');
    const [loading, setLoading] = useState(false);
    const [csrfToken, setCsrfToken] = useState('');
    const navigate = useNavigate();
    // Function to handle file selection
    const handleFileChange = (event) => {
        setFiles(event.target.files);
    };

    // Function to handle query input
    const handleQueryChange = (event) => {
        setQuery(event.target.value);
    };

    // Fetch CSRF token from a meta tag or other source
    // useEffect(() => {
    //     const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    //     setCsrfToken(token);
    // }, []);

    // Function to handle form submission
    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);

        const formData = new FormData();
        Array.from(files).forEach(file => formData.append('files', file));
        formData.append('query', query);

        try {
            const response = await fetch('http://localhost:8000/upload/', {
                method: 'POST',
                body: formData,
                // headers: {
                //     'X-CSRFToken': csrfToken,
                // },
            });

            const result = await response.json();
            const resultsId = result.results_id;
            const query = result.query;

            console.log(resultsId);
            console.log(query);

            // Redirect to results page
            navigate(`/results/${resultsId}/${query}/`)
            // window.location.href = `http://localhost:8000/results/${resultsId}/${query}/`;
        } catch (error) {
            console.error('Error:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className={styles.container}>
            <h1>Upload Files and Enter Query</h1>
            <form id="upload-form" onSubmit={handleSubmit}>
                <input
                    type="file"
                    name="files"
                    multiple
                    onChange={handleFileChange}
                />
                <input
                    type="text"
                    name="query"
                    placeholder="Enter query string"
                    required
                    value={query}
                    onChange={handleQueryChange}
                />
                <button type="submit" disabled={loading}>
                    {loading ? 'Uploading...' : 'Upload and Process'}
                </button>
            </form>
        </div>
    );
};

export default Form;
