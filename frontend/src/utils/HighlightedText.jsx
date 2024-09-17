import React from 'react';

const HighlightedText = ({ line, searchTerm }) => {
    if (!searchTerm) {
        return <span>{line}</span>;
    }

    // Find the index of the first occurrence of the search term
    const index = line.indexOf(searchTerm);

    if (index === -1) {
        // If searchTerm is not found, return the original line
        return <span>{line}</span>;
    }

    // Split the line into parts
    const beforeHighlight = line.substring(0, index);
    const highlighted = line.substring(index, index + searchTerm.length);
    const afterHighlight = line.substring(index + searchTerm.length);

    return (
        <>
            <span>{beforeHighlight}</span>
            <span style={{ backgroundColor: 'yellow' }}>{highlighted}</span>
            <span>{afterHighlight}</span>
        </>
    );
};

export default HighlightedText;
