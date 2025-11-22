'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { fetchProjects } from '@/lib/api';

export default function Home() {
  const [projects, setProjects] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProjects()
      .then(data => {
        setProjects(data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Projects</h1>
        <Link href="/projects/new" className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          New Project
        </Link>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {projects.map((project) => (
          <Link href={`/projects/${project.id}`} key={project.id} className="block p-6 bg-white rounded-lg border hover:shadow-lg transition">
            <h2 className="text-xl font-semibold mb-2">{project.title}</h2>
            <p className="text-gray-600 mb-4 line-clamp-2">{project.problem_to_solve}</p>
            <div className="flex justify-between text-sm text-gray-500">
              <span>{project.technical_field}</span>
              <span>{new Date(project.created_at).toLocaleDateString()}</span>
            </div>
          </Link>
        ))}
        {projects.length === 0 && (
          <div className="col-span-full text-center py-10 text-gray-500">
            No projects found. Create one to get started.
          </div>
        )}
      </div>
    </div>
  );
}
