/* ================================================================
   OUVIDORIA.AI – Frontend Script
   Futuristic CRUD Dashboard
   ================================================================ */

const API_BASE = '/api/reclamacoes';

// ---- DOM refs ----
const tableBody        = document.getElementById('tableBody');
const formNova         = document.getElementById('formNova');
const inputNova        = document.getElementById('inputNova');
const btnRefresh       = document.getElementById('btnRefresh');
const statTotalValue   = document.getElementById('statTotalValue');
const statBar          = document.getElementById('statBar');
const toastContainer   = document.getElementById('toastContainer');
const statusDot        = document.getElementById('statusDot');
const statusText       = document.getElementById('statusText');
const clockEl          = document.getElementById('clock');

// Edit modal
const editModal        = document.getElementById('editModal');
const editCodigo       = document.getElementById('editCodigo');
const editInput        = document.getElementById('editInput');
const btnCancelEdit    = document.getElementById('btnCancelEdit');
const btnSaveEdit      = document.getElementById('btnSaveEdit');

// Delete modal
const deleteModal      = document.getElementById('deleteModal');
const deleteCodigo     = document.getElementById('deleteCodigo');
const btnCancelDelete  = document.getElementById('btnCancelDelete');
const btnConfirmDelete = document.getElementById('btnConfirmDelete');

// Search
const inputSearch      = document.getElementById('inputSearch');
const btnSearch        = document.getElementById('btnSearch');
const searchResult     = document.getElementById('searchResult');
const searchResultBody = document.getElementById('searchResultBody');
const btnCloseSearch   = document.getElementById('btnCloseSearch');

let currentEditId = null;
let currentDeleteId = null;

// ================================================================
// CLOCK
// ================================================================
function updateClock() {
    const now = new Date();
    clockEl.textContent = now.toLocaleTimeString('pt-BR', { hour12: false });
}
setInterval(updateClock, 1000);
updateClock();

document.getElementById('year').textContent = new Date().getFullYear();

// ================================================================
// PARTICLE BACKGROUND
// ================================================================
(function initParticles() {
    const canvas = document.getElementById('particleCanvas');
    const ctx = canvas.getContext('2d');
    let particles = [];
    const MAX = 60;

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    class Particle {
        constructor() { this.reset(); }
        reset() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.vx = (Math.random() - 0.5) * 0.3;
            this.vy = (Math.random() - 0.5) * 0.3;
            this.r = Math.random() * 1.5 + 0.5;
            this.alpha = Math.random() * 0.4 + 0.1;
        }
        update() {
            this.x += this.vx;
            this.y += this.vy;
            if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
            if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(0, 240, 255, ${this.alpha})`;
            ctx.fill();
        }
    }

    for (let i = 0; i < MAX; i++) particles.push(new Particle());

    function drawLines() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 150) {
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(0, 240, 255, ${0.06 * (1 - dist / 150)})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            }
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => { p.update(); p.draw(); });
        drawLines();
        requestAnimationFrame(animate);
    }
    animate();
})();

// ================================================================
// TOAST
// ================================================================
function toast(msg, type = 'info') {
    const el = document.createElement('div');
    el.className = `toast toast--${type}`;
    const icons = { success: '✓', error: '✕', info: '●' };
    el.innerHTML = `<span>${icons[type] || '●'}</span> ${escapeHtml(msg)}`;
    toastContainer.appendChild(el);
    setTimeout(() => {
        el.style.animation = 'toastOut .3s ease forwards';
        el.addEventListener('animationend', () => el.remove());
    }, 3500);
}

// ================================================================
// HELPERS
// ================================================================
function escapeHtml(str) {
    const d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
}

function setServerStatus(online) {
    statusDot.className = online ? 'status-dot' : 'status-dot status-dot--off';
    statusText.textContent = online ? 'ONLINE' : 'OFFLINE';
}

// ================================================================
// SKELETON LOADER
// ================================================================
function showSkeleton(n = 5) {
    let html = '';
    for (let i = 0; i < n; i++) {
        const w = 40 + Math.random() * 45;
        html += `<tr>
            <td><div class="skeleton-bar" style="width:50px"></div></td>
            <td><div class="skeleton-bar" style="width:${w}%"></div></td>
            <td></td>
        </tr>`;
    }
    tableBody.innerHTML = html;
}

// ================================================================
// FETCH & RENDER
// ================================================================
async function carregarReclamacoes() {
    showSkeleton();
    try {
        const res = await fetch(API_BASE);
        if (!res.ok) throw new Error('Falha na requisição');
        const data = await res.json();
        setServerStatus(true);
        renderTable(data);
        statTotalValue.textContent = data.length;
        statBar.style.width = Math.min(data.length * 5, 100) + '%';
    } catch (err) {
        setServerStatus(false);
        tableBody.innerHTML = `<tr><td colspan="3">
            <div class="empty-state">
                <div class="empty-state__icon">⚠</div>
                <div class="empty-state__text">ERRO DE CONEXÃO COM O SERVIDOR</div>
            </div></td></tr>`;
        statTotalValue.textContent = '--';
        toast(err.message, 'error');
    }
}

function renderTable(data) {
    if (data.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="3">
            <div class="empty-state">
                <div class="empty-state__icon">📭</div>
                <div class="empty-state__text">NENHUMA RECLAMAÇÃO REGISTRADA</div>
            </div></td></tr>`;
        return;
    }
    tableBody.innerHTML = data.map(r => `
        <tr>
            <td class="td-code">#${r.codigo}</td>
            <td>${escapeHtml(r.reclamacao)}</td>
            <td class="td-actions">
                <button class="btn btn--outline btn--sm" onclick="openEdit(${r.codigo}, \`${escapeAttr(r.reclamacao)}\`)">✏️ EDITAR</button>
                <button class="btn btn--danger btn--sm" onclick="openDelete(${r.codigo})">🗑 EXCLUIR</button>
            </td>
        </tr>`).join('');
}

function escapeAttr(str) {
    return str.replace(/\\/g, '\\\\').replace(/`/g, '\\`').replace(/\$/g, '\\$');
}

// ================================================================
// CREATE
// ================================================================
formNova.addEventListener('submit', async (e) => {
    e.preventDefault();
    const texto = inputNova.value.trim();
    if (!texto) return;

    const btn = document.getElementById('btnSubmit');
    btn.disabled = true;

    try {
        const res = await fetch(API_BASE, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ reclamacao: texto }),
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.erro || 'Erro ao registrar');
        toast(`Reclamação #${data.codigo} registrada com sucesso!`, 'success');
        inputNova.value = '';
        carregarReclamacoes();
    } catch (err) {
        toast(err.message, 'error');
    } finally {
        btn.disabled = false;
    }
});

// ================================================================
// SEARCH
// ================================================================
btnSearch.addEventListener('click', async () => {
    const codigo = inputSearch.value.trim();
    if (!codigo) return toast('Informe um código para pesquisar.', 'error');

    try {
        const res = await fetch(`${API_BASE}/${codigo}`);
        const data = await res.json();
        if (!res.ok) throw new Error(data.erro || 'Não encontrada');

        searchResultBody.innerHTML = `
            <div style="margin-bottom:.4rem">
                <span style="color:var(--neon);font-family:var(--mono);font-weight:700">#${data.codigo}</span>
            </div>
            <div style="color:var(--text)">${escapeHtml(data.reclamacao)}</div>`;
        searchResult.hidden = false;
    } catch (err) {
        toast(err.message, 'error');
        searchResult.hidden = true;
    }
});

inputSearch.addEventListener('keydown', (e) => { if (e.key === 'Enter') btnSearch.click(); });
btnCloseSearch.addEventListener('click', () => { searchResult.hidden = true; });

// ================================================================
// EDIT
// ================================================================
function openEdit(codigo, texto) {
    currentEditId = codigo;
    editCodigo.textContent = `#${codigo}`;
    editInput.value = texto;
    editModal.hidden = false;
    setTimeout(() => editInput.focus(), 100);
}

btnCancelEdit.addEventListener('click', () => { editModal.hidden = true; });
editModal.addEventListener('click', (e) => { if (e.target === editModal) editModal.hidden = true; });

btnSaveEdit.addEventListener('click', async () => {
    const novoTexto = editInput.value.trim();
    if (!novoTexto) return toast('A reclamação não pode ser vazia.', 'error');

    btnSaveEdit.disabled = true;
    try {
        const res = await fetch(`${API_BASE}/${currentEditId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ reclamacao: novoTexto }),
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.erro || 'Erro ao atualizar');
        toast('Reclamação atualizada com sucesso!', 'success');
        editModal.hidden = true;
        carregarReclamacoes();
    } catch (err) {
        toast(err.message, 'error');
    } finally {
        btnSaveEdit.disabled = false;
    }
});

// ================================================================
// DELETE
// ================================================================
function openDelete(codigo) {
    currentDeleteId = codigo;
    deleteCodigo.textContent = `#${codigo}`;
    deleteModal.hidden = false;
}

btnCancelDelete.addEventListener('click', () => { deleteModal.hidden = true; });
deleteModal.addEventListener('click', (e) => { if (e.target === deleteModal) deleteModal.hidden = true; });

btnConfirmDelete.addEventListener('click', async () => {
    btnConfirmDelete.disabled = true;
    try {
        const res = await fetch(`${API_BASE}/${currentDeleteId}`, { method: 'DELETE' });
        const data = await res.json();
        if (!res.ok) throw new Error(data.erro || 'Erro ao remover');
        toast('Reclamação removida com sucesso!', 'success');
        deleteModal.hidden = true;
        carregarReclamacoes();
    } catch (err) {
        toast(err.message, 'error');
    } finally {
        btnConfirmDelete.disabled = false;
    }
});

// ================================================================
// REFRESH
// ================================================================
btnRefresh.addEventListener('click', () => {
    btnRefresh.disabled = true;
    carregarReclamacoes().finally(() => { btnRefresh.disabled = false; });
});

// ================================================================
// INIT
// ================================================================
carregarReclamacoes();
