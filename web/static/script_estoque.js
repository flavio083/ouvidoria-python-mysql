const API_BASE = '/api/produtos';

// ===== PARTICLES BACKGROUND =====
(function initParticles() {
    const canvas = document.getElementById('particleCanvas');
    if (!canvas) return;
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
            this.x += this.vx; this.y += this.vy;
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

// ===== UTILITIES =====
function toast(msg, type = 'info') {
    const toastContainer = document.getElementById('toastContainer');
    if (!toastContainer) return;
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

function escapeHtml(str) {
    const d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
}

function escapeAttr(str) {
    return String(str).replace(/\\/g, '\\\\').replace(/`/g, '\\`').replace(/\$/g, '\\$').replace(/"/g, '&quot;');
}

function formatBRL(value) {
    return Number(value).toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

// ===== MAIN =====
document.addEventListener('DOMContentLoaded', () => {

    // DOM refs
    const tableBody       = document.getElementById('tableBody');
    const formNovo        = document.getElementById('formNovo');
    const btnRefresh      = document.getElementById('btnRefresh');
    const statTotal       = document.getElementById('statTotalValue');
    const statItens       = document.getElementById('statItensValue');
    const statValor       = document.getElementById('statValorValue');
    const statBar         = document.getElementById('statBar');
    const statusDot       = document.getElementById('statusDot');
    const statusText      = document.getElementById('statusText');
    const clockEl         = document.getElementById('clock');
    const alertBadge      = document.getElementById('alertBadge');

    const editModal       = document.getElementById('editModal');
    const editId          = document.getElementById('editId');
    const editNome        = document.getElementById('editNome');
    const editCategoria   = document.getElementById('editCategoria');
    const editQuantidade  = document.getElementById('editQuantidade');
    const editPreco       = document.getElementById('editPreco');
    const editFornecedor  = document.getElementById('editFornecedor');
    const btnCancelEdit   = document.getElementById('btnCancelEdit');
    const btnSaveEdit     = document.getElementById('btnSaveEdit');

    const deleteModal      = document.getElementById('deleteModal');
    const deleteId         = document.getElementById('deleteId');
    const btnCancelDelete  = document.getElementById('btnCancelDelete');
    const btnConfirmDelete = document.getElementById('btnConfirmDelete');

    let currentEditId   = null;
    let currentDeleteId = null;

    // ===== CLOCK =====
    if (clockEl) {
        function updateClock() {
            clockEl.textContent = new Date().toLocaleTimeString('pt-BR', { hour12: false });
        }
        setInterval(updateClock, 1000);
        updateClock();
    }

    const yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    // ===== STATUS =====
    function setServerStatus(online) {
        if (statusDot) statusDot.className = online ? 'status-dot' : 'status-dot status-dot--off';
        if (statusText) statusText.textContent = online ? 'ONLINE' : 'OFFLINE';
    }

    // ===== SKELETON =====
    function showSkeleton(n = 5) {
        if (!tableBody) return;
        let html = '';
        for (let i = 0; i < n; i++) {
            html += `<tr>
                <td><div class="skeleton-bar" style="width:40px"></div></td>
                <td><div class="skeleton-bar" style="width:${40 + Math.random() * 40}%"></div></td>
                <td><div class="skeleton-bar" style="width:80px"></div></td>
                <td><div class="skeleton-bar" style="width:50px"></div></td>
                <td><div class="skeleton-bar" style="width:70px"></div></td>
                <td><div class="skeleton-bar" style="width:90px"></div></td>
                <td></td>
            </tr>`;
        }
        tableBody.innerHTML = html;
    }

    // ===== LOAD DATA =====
    async function carregarProdutos() {
        showSkeleton();
        try {
            const [resProdutos, resumo] = await Promise.all([
                fetch(API_BASE),
                fetch(`${API_BASE}/resumo`),
            ]);

            if (!resProdutos.ok) throw new Error('Falha na requisição');

            const produtos = await resProdutos.json();
            const res = await resumo.json();

            setServerStatus(true);
            renderTable(produtos);

            if (statTotal) statTotal.textContent = res.total_produtos ?? '--';
            if (statItens) statItens.textContent = res.total_itens ?? '--';
            if (statValor) statValor.textContent = res.valor_total != null ? `R$ ${formatBRL(res.valor_total)}` : '--';
            if (statBar)   statBar.style.width = Math.min((res.total_produtos || 0) * 5, 100) + '%';

            // Alerta de estoque baixo
            const resAlerta = await fetch(`${API_BASE}/alerta?limite=5`);
            const alertas = await resAlerta.json();
            if (alertBadge) {
                alertBadge.textContent = alertas.length;
                alertBadge.hidden = alertas.length === 0;
            }

        } catch (err) {
            setServerStatus(false);
            if (tableBody) {
                tableBody.innerHTML = `<tr><td colspan="7">
                    <div class="empty-state">
                        <div class="empty-state__icon">⚠</div>
                        <div class="empty-state__text">ERRO DE CONEXÃO COM O SERVIDOR</div>
                    </div></td></tr>`;
            }
            if (statTotal) statTotal.textContent = '--';
            toast(err.message, 'error');
        }
    }

    function renderTable(data) {
        if (!tableBody) return;
        if (data.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="7">
                <div class="empty-state">
                    <div class="empty-state__icon">📦</div>
                    <div class="empty-state__text">NENHUM PRODUTO CADASTRADO</div>
                </div></td></tr>`;
            return;
        }

        tableBody.innerHTML = data.map(p => {
            const baixo = p.quantidade <= 5;
            return `<tr>
                <td class="td-code">#${p.id}</td>
                <td>${escapeHtml(p.nome)}</td>
                <td><span class="badge badge--cat">${escapeHtml(p.categoria)}</span></td>
                <td class="${baixo ? 'td-low' : ''}">${p.quantidade}${baixo ? ' ⚠' : ''}</td>
                <td>R$ ${formatBRL(p.preco)}</td>
                <td>${escapeHtml(p.fornecedor)}</td>
                <td class="td-actions">
                    <button class="btn btn--outline btn--sm" onclick="openEdit(${p.id}, \`${escapeAttr(p.nome)}\`, \`${escapeAttr(p.categoria)}\`, ${p.quantidade}, ${p.preco}, \`${escapeAttr(p.fornecedor)}\`)">✏️ EDITAR</button>
                    <button class="btn btn--danger btn--sm" onclick="openDelete(${p.id})">🗑 EXCLUIR</button>
                </td>
            </tr>`;
        }).join('');
    }

    // ===== MODAL FUNCTIONS (global so inline onclick works) =====
    window.openEdit = function(id, nome, categoria, quantidade, preco, fornecedor) {
        if (!editModal || !editId || !editNome) return;
        currentEditId = id;
        editId.textContent = `#${id}`;
        editNome.value = nome;
        editCategoria.value = categoria;
        editQuantidade.value = quantidade;
        editPreco.value = preco;
        editFornecedor.value = fornecedor;
        editModal.hidden = false;
        setTimeout(() => editNome.focus(), 100);
    };

    window.openDelete = function(id) {
        if (!deleteModal || !deleteId) return;
        currentDeleteId = id;
        deleteId.textContent = `#${id}`;
        deleteModal.hidden = false;
    };

    // ===== EVENT LISTENERS =====
    if (formNovo) {
        formNovo.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('btnSubmit');
            if (!btn) return;
            btn.disabled = true;

            const payload = {
                nome:       document.getElementById('inputNome')?.value.trim() || '',
                categoria:  document.getElementById('inputCategoria')?.value.trim() || '',
                quantidade: document.getElementById('inputQuantidade')?.value || 0,
                preco:      document.getElementById('inputPreco')?.value || 0,
                fornecedor: document.getElementById('inputFornecedor')?.value.trim() || '',
            };

            try {
                const res = await fetch(API_BASE, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload),
                });
                const data = await res.json();
                if (!res.ok) throw new Error(data.erro || 'Erro ao cadastrar');
                toast(`Produto #${data.id} cadastrado com sucesso!`, 'success');
                formNovo.reset();
                carregarProdutos();
            } catch (err) {
                toast(err.message, 'error');
            } finally {
                btn.disabled = false;
            }
        });
    }

    if (btnCancelEdit) btnCancelEdit.addEventListener('click', () => { if (editModal) editModal.hidden = true; });
    if (editModal)     editModal.addEventListener('click', (e) => { if (e.target === editModal) editModal.hidden = true; });

    if (btnSaveEdit) {
        btnSaveEdit.addEventListener('click', async () => {
            btnSaveEdit.disabled = true;
            const payload = {
                nome:       editNome?.value.trim() || '',
                categoria:  editCategoria?.value.trim() || '',
                quantidade: editQuantidade?.value || 0,
                preco:      editPreco?.value || 0,
                fornecedor: editFornecedor?.value.trim() || '',
            };
            try {
                const res = await fetch(`${API_BASE}/${currentEditId}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload),
                });
                const data = await res.json();
                if (!res.ok) throw new Error(data.erro || 'Erro ao atualizar');
                toast('Produto atualizado com sucesso!', 'success');
                if (editModal) editModal.hidden = true;
                carregarProdutos();
            } catch (err) {
                toast(err.message, 'error');
            } finally {
                btnSaveEdit.disabled = false;
            }
        });
    }

    if (btnCancelDelete) btnCancelDelete.addEventListener('click', () => { if (deleteModal) deleteModal.hidden = true; });
    if (deleteModal)     deleteModal.addEventListener('click', (e) => { if (e.target === deleteModal) deleteModal.hidden = true; });

    if (btnConfirmDelete) {
        btnConfirmDelete.addEventListener('click', async () => {
            btnConfirmDelete.disabled = true;
            try {
                const res = await fetch(`${API_BASE}/${currentDeleteId}`, { method: 'DELETE' });
                const data = await res.json();
                if (!res.ok) throw new Error(data.erro || 'Erro ao remover');
                toast('Produto removido com sucesso!', 'success');
                if (deleteModal) deleteModal.hidden = true;
                carregarProdutos();
            } catch (err) {
                toast(err.message, 'error');
            } finally {
                btnConfirmDelete.disabled = false;
            }
        });
    }

    if (btnRefresh) {
        btnRefresh.addEventListener('click', () => {
            btnRefresh.disabled = true;
            carregarProdutos().finally(() => { if (btnRefresh) btnRefresh.disabled = false; });
        });
    }

    // ===== SIDEBAR =====
    (function initSidebar() {
        const sidebar = document.getElementById('sidebar');
        const toggle  = document.getElementById('sidebarToggle');
        if (!sidebar || !toggle) return;

        const overlay = document.createElement('div');
        overlay.className = 'sidebar-overlay';
        document.body.appendChild(overlay);

        function openSidebar()  { sidebar.classList.add('sidebar--open');    overlay.classList.add('sidebar-overlay--visible'); }
        function closeSidebar() { sidebar.classList.remove('sidebar--open'); overlay.classList.remove('sidebar-overlay--visible'); }

        toggle.addEventListener('click', () => {
            sidebar.classList.contains('sidebar--open') ? closeSidebar() : openSidebar();
        });
        overlay.addEventListener('click', closeSidebar);
    })();

    // ===== INIT =====
    carregarProdutos();
});
