# Router 层测试计划

**版本**: v2026-04-16  
**日期**: 2026-04-16

## 一、测试目标

验证 Router 层的多提供商路由功能：

| 组件 | 职责 |
|------|------|
| `RouterLayer` | 路由到不同提供商和模型层级 |
| `get_model()` | 根据 provider+type 返回模型名 |
| `route_request()` | 支持 type 路由和智能路由 |
| `auto_route()` | 根据输入复杂度自动选择层级 |

---

## 二、测试用例

### 2.1 Type 路由测试

#### TC001: Anthropic 各层级模型路由
| 字段 | 内容 |
|------|------|
| 用例 ID | TC001 |
| 用例名称 | Anthropic 各层级模型路由 |
| 输入数据 | provider="anthropic", type="high/medium/low" |
| 预期结果 | 返回对应的 claude-opus/sonnet/haiku 模型 |

#### TC002: OpenAI 各层级模型路由
| 字段 | 内容 |
|------|------|
| 用例 ID | TC002 |
| 用例名称 | OpenAI 各层级模型路由 |
| 输入数据 | provider="openai", type="high/medium/low" |
| 预期结果 | 返回对应的 gpt-4.5/gpt-4o/gpt-4o-mini 模型 |

#### TC003: 提供商别名解析
| 字段 | 内容 |
|------|------|
| 用例 ID | TC003 |
| 用例名称 | 提供商别名解析 |
| 输入数据 | provider="claude/gpt/gemini" |
| 预期结果 | 正确解析为 anthropic/openai/google |

### 2.2 智能路由测试

#### TC004: 短输入使用低端模型
| 字段 | 内容 |
|------|------|
| 用例 ID | TC004 |
| 用例名称 | 短输入使用 low 层级 |
| 输入数据 | 输入<50 字 |
| 预期结果 | 返回 low 层级模型 |

#### TC005: 中等输入使用中端模型
| 字段 | 内容 |
|------|------|
| 用例 ID | TC005 |
| 用例名称 | 中等输入使用 medium 层级 |
| 输入数据 | 输入 50-200 字 |
| 预期结果 | 返回 medium 层级模型 |

#### TC006: 长输入使用高端模型
| 字段 | 内容 |
|------|------|
| 用例 ID | TC006 |
| 用例名称 | 长输入使用 high 层级 |
| 输入数据 | 输入>200 字 |
| 预期结果 | 返回 high 层级模型 |

### 2.3 Completion 测试

#### TC007: 调用 LiteLLM Completion
| 字段 | 内容 |
|------|------|
| 用例 ID | TC007 |
| 用例名称 | 调用 LiteLLM completion |
| 输入数据 | 有效的 model 和 messages |
| 预期结果 | 返回 LLM 响应 |

---

## 三、测试结果记录模板

| 用例 ID | 状态 | 耗时 | 备注 |
|---------|------|------|------|
| TC001 | [ ] PASS [ ] FAIL | - | - |
| TC002 | [ ] PASS [ ] FAIL | - | - |
| ... | ... | ... | ... |

---

## 四、运行方式

```bash
# 运行全部测试
python tests/test_router.py

# 运行单个测试用例
python -m pytest tests/test_router.py::test_anthropic_routing -v
```