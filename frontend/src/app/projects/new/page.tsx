'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { createProject } from '@/lib/api';

export default function NewProject() {
    const router = useRouter();
    const [formData, setFormData] = useState({
        title: '',
        invention_title: '',
        technical_field: '',
        problem_to_solve: '',
        technical_solution: '',
    });

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            await createProject(formData);
            router.push('/');
        } catch (err) {
            console.error(err);
            alert('Failed to create project');
        }
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    return (
        <div className="max-w-2xl mx-auto">
            <h1 className="text-3xl font-bold mb-6">New Project</h1>
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label className="block text-sm font-medium mb-1">Project Title</label>
                    <input
                        name="title"
                        value={formData.title}
                        onChange={handleChange}
                        className="w-full border rounded p-2"
                        required
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium mb-1">Invention Title</label>
                    <input
                        name="invention_title"
                        value={formData.invention_title}
                        onChange={handleChange}
                        className="w-full border rounded p-2"
                        required
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium mb-1">Technical Field</label>
                    <input
                        name="technical_field"
                        value={formData.technical_field}
                        onChange={handleChange}
                        className="w-full border rounded p-2"
                        required
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium mb-1">Problem to Solve</label>
                    <textarea
                        name="problem_to_solve"
                        value={formData.problem_to_solve}
                        onChange={handleChange}
                        className="w-full border rounded p-2 h-32"
                        required
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium mb-1">Technical Solution</label>
                    <textarea
                        name="technical_solution"
                        value={formData.technical_solution}
                        onChange={handleChange}
                        className="w-full border rounded p-2 h-32"
                        required
                    />
                </div>
                <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
                    Create Project
                </button>
            </form>
        </div>
    );
}
