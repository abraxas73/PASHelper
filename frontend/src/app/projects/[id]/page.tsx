'use client';

import { useState, useEffect } from 'react';
import { useParams } from 'next/navigation';
import { searchKipris } from '@/lib/api';

export default function ProjectDetail() {
    const params = useParams();
    const [keywords, setKeywords] = useState('');
    const [results, setResults] = useState<any[]>([]);
    const [loading, setLoading] = useState(false);

    const handleSearch = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        try {
            const keywordList = keywords.split(',').map(k => k.trim());
            const data = await searchKipris(keywordList);
            setResults(data);
        } catch (err) {
            console.error(err);
            alert('Search failed');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="space-y-8">
            <div className="flex justify-between items-center">
                <h1 className="text-3xl font-bold">Project Detail</h1>
                <span className="text-gray-500">ID: {params.id}</span>
            </div>

            <div className="bg-white p-6 rounded-lg border">
                <h2 className="text-xl font-semibold mb-4">Prior Art Search</h2>
                <form onSubmit={handleSearch} className="flex gap-4 mb-6">
                    <input
                        value={keywords}
                        onChange={(e) => setKeywords(e.target.value)}
                        placeholder="Enter keywords (comma separated)"
                        className="flex-1 border rounded p-2"
                    />
                    <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700" disabled={loading}>
                        {loading ? 'Searching...' : 'Search'}
                    </button>
                </form>

                <div className="space-y-4">
                    {results.map((result, idx) => (
                        <div key={idx} className="border p-4 rounded hover:bg-gray-50">
                            <h3 className="font-bold text-lg text-blue-600">{result.title}</h3>
                            <div className="text-sm text-gray-500 mb-2">
                                {result.publication_number} | {result.applicant} | {result.publication_date}
                            </div>
                            <p className="text-gray-700">{result.abstract}</p>
                        </div>
                    ))}
                    {results.length === 0 && !loading && (
                        <div className="text-center text-gray-500">No search results yet.</div>
                    )}
                </div>
            </div>
        </div>
    );
}
