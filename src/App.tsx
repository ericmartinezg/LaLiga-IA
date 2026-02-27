/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

export default function App() {
  return (
    <div className="min-h-screen bg-slate-900 text-white flex flex-col items-center justify-center p-8">
      <div className="max-w-2xl bg-slate-800 p-8 rounded-2xl shadow-2xl border border-slate-700 text-center">
        <div className="w-16 h-16 bg-emerald-500/20 text-emerald-400 rounded-full flex items-center justify-center mx-auto mb-6 text-3xl">
          🐍
        </div>
        <h1 className="text-3xl font-bold mb-4">¡Archivos de Streamlit Generados!</h1>
        <p className="text-slate-300 mb-8 text-lg">
          He creado los archivos Python para tu aplicación de Streamlit basándome en tu diseño de Tailwind CSS.
        </p>
        
        <div className="text-left bg-slate-900 p-6 rounded-xl border border-slate-700 mb-8">
          <h2 className="text-emerald-400 font-semibold mb-4">Archivos generados:</h2>
          <ul className="space-y-3">
            <li className="flex items-center gap-3">
              <span className="text-xl">📄</span>
              <code className="bg-slate-800 px-2 py-1 rounded text-emerald-300">app.py</code>
              <span className="text-slate-400 text-sm">- Predictor principal</span>
            </li>
            <li className="flex items-center gap-3">
              <span className="text-xl">📁</span>
              <code className="bg-slate-800 px-2 py-1 rounded text-emerald-300">pages/resultados.py</code>
              <span className="text-slate-400 text-sm">- Historial de resultados</span>
            </li>
          </ul>
        </div>

        <p className="text-slate-400 text-sm">
          Puedes descargar estos archivos desde el panel de archivos a la izquierda y desplegarlos directamente en Streamlit Community Cloud.
        </p>
      </div>
    </div>
  );
}
