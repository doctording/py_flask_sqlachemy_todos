数据库连接池 和 Sqlachemy

## 数据库连接池

<a href="https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E5%BA%93%E8%BF%9E%E6%8E%A5%E6%B1%A0/1518538" target="_blank">数据库连接池百度百科</a>

数据库连接池负责分配、管理和释放数据库连接，它允许应用程序重复使用一个现有的数据库连接，而不是再重新建立一个；释放空闲时间超过最大空闲时间的数据库连接来避免因为没有释放数据库连接而引起的数据库连接遗漏。这项技术能明显提高对数据库操作的性能。

数据库连接池在初始化时将创建一定数量的数据库连接放到连接池中，这些数据库连接的数量是由`最小数据库连接`数制约。无论这些数据库连接是否被使用，连接池都将一直保证至少拥有这么多的连接数量。连接池的最大数据库连接数量限定了这个连接池能占有的`最大连接数`，当应用程序向连接池请求的连接数超过最大连接数量时，这些请求将被加入到等待队列中。数据库连接池的最小连接数和最大连接数的设置要考虑到下列几个因素：

1. 最小连接数

是连接池一直保持的数据库连接，所以如果应用程序对数据库连接的使用量不大，将会有大量的数据库连接资源被浪费。

2. 最大连接数

是连接池能申请的最大连接数，如果数据库连接请求超过此数，后面的数据库连接请求将被加入到等待队列中，这会影响之后的数据库操作。

3. 最小连接数与最大连接数差距

最小连接数与最大连接数相差太大，那么最先的连接请求将会获利，之后超过最小连接数量的连接请求等价于建立一个新的数据库连接。不过，这些大于最小连接数的数据库连接在使用完不会马上被释放，它将被放到连接池中等待重复使用或是空闲超时后被释放。

参考博文： https://www.cnblogs.com/wym789/p/6374440.html

数据库连接池技术带来的优势：(可以对比`线程池`之类的)

1. 资源重用

由于数据库连接得到重用，避免了频繁创建、释放连接引起的大量性能开销(对于需要大并发量的复杂数据库应用)。在减少系统消耗的基础上，另一方面也增进了系统运行环境的平稳性（减少内存碎片以及数据库临时进程/线程的数量）。(如MySQL连接是tcp，如果系统出现大量的tcp连接，无疑是消耗性能的)

2． 更快的系统响应速度

数据库连接池在初始化过程中，往往已经创建了若干数据库连接置于池中备用。此时连接的初始化工作均已完成。对于业务请求处理而言，直接利用现有可用连接，避免了数据库连接初始化和释放过程的时间开销，从而缩减了系统整体响应时间。

3． 新的资源分配手段

对于多应用共享同一数据库的系统而言，可在应用层通过数据库连接的配置，实现数据库连接池技术。如限制某一应用最大可用数据库连接数，避免某一应用独占所有数据库资源。

4． 统一的连接管理，避免数据库连接泄漏

在较为完备的数据库连接池实现中，可根据预先的连接占用超时设定，强制收回被占用连接。从而避免了常规数据库连接操作中可能出现的资源泄漏。

## Sqlachemy

https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlalchemy.create_engine


### create_engine 重要参数说明

https://docs.sqlalchemy.org/en/latest/core/engines.html#engine-creation-api

* **max_overflow=10** – the number of connections to allow in connection pool “overflow”, that is connections that can be opened above and beyond the pool_size setting, which defaults to five. this is only used with `QueuePool`.

* **pool=None** – an already-constructed instance of `Pool`, such as a `QueuePool` instance. If non-None, this pool will be used directly as the underlying connection pool for the engine, bypassing whatever connection parameters are present in the URL argument. For information on constructing connection pools manually, see `Connection Pooling`.


* **poolclass=None** – a `Pool` subclass, which will be used to create a connection pool instance using the connection parameters given in the URL. Note this differs from `pool` in that you don’t actually instantiate the pool in this case, you just indicate what type of pool to be used.

* **pool_size=5** – the number of connections to keep open inside the connection pool. This used with `QueuePool` as well as `SingletonThreadPool`. With `QueuePool`, a `pool_size` setting of 0 indicates no limit; to disable pooling, set `poolclass` to `NullPool` instead.

* **pool_recycle=-1** - this setting causes the pool to recycle connections after the given number of seconds has passed. It defaults to -1, or no timeout. For example, setting to 3600 means connections will be recycled after one hour. Note that MySQL in particular will disconnect automatically if no activity is detected on a connection for eight hours (although this is configurable with the MySQLDB connection itself and the server configuration as well).

* **pool_timeout=30** – number of seconds to wait before giving up on getting a connection from the pool. This is only used with `QueuePool`.


## Session and sessionmaker()

https://docs.sqlalchemy.org/en/latest/orm/session_api.html?highlight=sessionmaker#session-and-sessionmaker

* sessionmaker

```python
class sqlalchemy.orm.session.sessionmaker(bind=None, class_=<class 'sqlalchemy.orm.session.Session'>, autoflush=True, autocommit=False, expire_on_commit=True, info=None, **kw)

# Bases: sqlalchemy.orm.session._SessionClassMethods
```

A configurable `Session` factory.

The `sessionmaker` factory generates new `Session` objects when called, creating them given the configurational arguments established here.

* Session

```python
class sqlalchemy.orm.session.Session(bind=None, autoflush=True, expire_on_commit=True, _enable_transaction_accounting=True, autocommit=False, twophase=False, weak_identity_map=True, binds=None, extension=None, enable_baked_queries=True, info=None, query_cls=<class 'sqlalchemy.orm.query.Query'>)

# Bases: sqlalchemy.orm.session._SessionClassMethods
```

Manages persistence operations for ORM-mapped objects.

session的详解需阅读：https://docs.sqlalchemy.org/en/latest/orm/session.html


### QueuePool

```python
class sqlalchemy.pool.QueuePool(creator, pool_size=5, max_overflow=10, timeout=30, **kw)

# Bases: sqlalchemy.pool.Pool
```

Parameters: (构建`QueuePool`的参数说明)

* **creator** – a callable function that returns a DB-API connection object, same as that of Pool.creator.

* **pool_size** – The size of the pool to be maintained, defaults to 5. This is the largest number of connections that will be kept persistently in the pool. Note that the pool begins with no connections; once this number of connections is requested, that number of connections will remain. `pool_size` can be set to 0 to indicate no size limit; to disable pooling, use a `NullPool` instead.

* **max_overflow** – The maximum overflow size of the pool. When the number of checked-out connections reaches the size set in pool_size, additional connections will be returned up to this limit. When those additional connections are returned to the pool, they are disconnected and discarded. It follows then that the total number of simultaneous connections the pool will allow is pool_size + max_overflow, and the total number of “sleeping” connections the pool will allow is pool_size. max_overflow can be set to -1 to indicate no overflow limit; no limit will be placed on the total number of concurrent connections. Defaults to 10.

* **timeout** – The number of seconds to wait before giving up on returning a connection. Defaults to 30.

* **\*\*kw** – Other keyword arguments including Pool.recycle, Pool.echo, `Pool.reset_on_return` and others are passed to the `Pool` constructor.


`connect()`

```
inherited from the connect() method of Pool
```

Return a DBAPI connection from the pool.

The connection is instrumented such that when its `close()` method is called, the connection will be returned to the `pool`.

### NullPool

```python
class sqlalchemy.pool.NullPool(creator, recycle=-1, echo=None, use_threadlocal=False, logging_name=None, reset_on_return=True, listeners=None, events=None, dialect=None, pre_ping=False, _dispatch=None)

# Bases: sqlalchemy.pool.Pool
```

A Pool which does not pool connections.

Instead it literally opens and closes the underlying DB-API connection per each connection open/close.

Reconnect-related functions such as `recycle` and connection invalidation are not supported by this Pool implementation, since no connections are held persistently.