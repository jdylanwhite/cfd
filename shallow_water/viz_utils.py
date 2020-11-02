def contour_plots(x,y,u,v,h,time):

    '''Plot contours for u, v, and h at a specified time step'''

    # Initiate figure and adjust for colorbars
    fig,ax = plt.subplots(1,3,figsize=(20,6),constrained_layout=True);
    fig.subplots_adjust(left=0.02, bottom=0.06, right=0.95, top=0.85, wspace=0.15);
    fig.suptitle("Time: {:.2f} hours".format(time/3600),fontsize=22);

    # Plot u
    contourf = ax[0].contourf(x/1000.,y/1000.,u,cmap=cm.coolwarm,vmin=-0.25,vmax=0.25);
    ax[0].set_xlabel("$x$ [km]",fontsize=14);
    ax[0].set_ylabel("$y$ [km]",fontsize=14);
    ax[0].set_title(f"$u$",fontsize=18);
    cbar = fig.colorbar(contourf, ax=ax[0]);
    cbar.set_clim(-0.25,0.25)

    # Plot v
    contourf = ax[1].contourf(x/1000.,y/1000.,v,cmap=cm.coolwarm,vmin=-0.25,vmax=0.25);
    ax[1].set_xlabel("$x$ [km]",fontsize=14);
    ax[1].set_title(f"$v$",fontsize=18);
    fig.colorbar(contourf, ax=ax[1]);

    # Plot h
    contourf = ax[2].contourf(x/1000.,y/1000.,h,cmap=cm.coolwarm,vmin=H-1,vmax=H+1);
    ax[2].set_xlabel("$x$ [km]",fontsize=14);
    ax[2].set_title(f"$h$",fontsize=18);
    fig.colorbar(contourf, ax=ax[2]);    

def surface_plot(x,y,h,time,vmin,vmax):

    '''Plot surface for h at a specified time step'''

    # Create the plot
    fig = plt.figure(figsize=(16,8));
    ax = fig.gca(projection='3d');
    ax.set_zlim(H-1,H+1);
    surf = ax.plot_surface(x/1000.,y/1000.,h,vmin=vmin,vmax=vmax,linewidth=2.0,cmap=cm.coolwarm);
    ax.set_title("Time: {:.2f} hours".format(time/3600),fontsize=22);
    ax.set_xlabel("$x$ [km]",fontsize=14);
    ax.set_ylabel("$y$ [km]",fontsize=14);
    fig.colorbar(surf, shrink=0.5, aspect=5);

def quiver_plot(x,y,u,v,time,stride=4):

    """Plot the flow u,v at a specified time"""

    # Create the plot
    plt.figure(figsize=(12,12))
    plt.title("Flow at Time:  {:.2f} hours".format(time/3600),fontsize=22)
    plt.xlabel("x [km]",fontsize=14)
    plt.ylabel("y [km]",fontsize=14)
    Q = plt.quiver(x[::stride, ::stride]/1000.,y[::stride,::stride]/1000., 
                   u[::stride, ::stride],v[::stride,::stride],
                   units="xy",scale = 0.2,scale_units="inches")
    qk = plt.quiverkey(Q,0.86,0.895,0.1, 
                       label="0.1 m/s",labelpos="W",
                       coordinates="figure",fontproperties={'size':14})

def eta_animation(X,Y,eta_list,dt,fileName,sample_interal,interval=1):

    '''Plot contour for eta at specified time'''

    fig,ax = plt.subplots(figsize=(10,10));
    contourf = ax.contourf(X/1000.,Y/1000.,eta_list[int(len(eta_list)/2)],cmap=cm.coolwarm,
            vmin=-0.7*np.abs(eta_list[int(len(eta_list)/2)]).max(),
            vmax=np.abs(eta_list[int(len(eta_list)/2)]).max())
    ax.set_xlabel('$x$ [km]',fontsize=14);
    ax.set_ylabel('$y$ [km]',fontsize=14);
    fig.colorbar(contourf);

    def animate(n,eta_list,sample_interval,dt):
        contourf = ax.contourf(X/1000.,Y/1000.,eta_list[n],cmap=cm.coolwarm,
            vmin=-0.7*np.abs(eta_list[int(len(eta_list)/2)]).max(),
            vmax=np.abs(eta_list[int(len(eta_list)/2)]).max());
        ax.set_title('Surface elevation $\eta$ at time = {:.2f} hours'.format(n*sample_interval*dt/3600.),fontsize=18);
        return contourf
        for coll in contourf.collections: 
            plt.gca().collections.remove(coll) 

    anim = animation.FuncAnimation(fig,animate,frames=range(0,len(eta_list),interval),fargs=(eta_list,sample_interval,dt))
    anim.save("{}.gif".format(fileName),writer='imagemagick',fps=20)

def quiver_animation(X,Y,u_list,v_list,dt,fileName,sample_interval,interval=1,stride=4):

    '''Plot the flow vectors at a specified time'''

    fig,ax = plt.subplots(figsize=(10,10));
    Q = plt.quiver(X[::stride, ::stride]/1000.,Y[::stride,::stride]/1000., 
                   u_list[0][::stride, ::stride],v_list[0][::stride,::stride],
                   units="xy",scale = 0.2,scale_units="inches");
    qk = plt.quiverkey(Q,0.86,0.895,0.1, 
                       label="0.1 m/s",labelpos="W",
                       coordinates="figure",fontproperties={'size':14});
    ax.set_xlabel('$x$ [km]',fontsize=14);
    ax.set_ylabel('$y$ [km]',fontsize=14);

    # animation function
    def animate(n,eta_list,dt):
        ax.set_title('Flow at time = {:.2f} hours'.format(n*sample_interval*dt/3600.),fontsize=18)
        Q.set_UVC(u_list[n][::stride, ::stride],v_list[n][::stride,::stride])
        return Q,

    anim = animation.FuncAnimation(fig,animate,frames=range(0,len(u_list),interval),fargs=(u_list,dt))
    anim.save("{}.gif".format(fileName),writer='imagemagick',fps=20)

def surface_animation(X,Y,eta_list,H,dt,fileName,sample_interval,interval=1):

    '''Plot animated surface h for all times'''

    def animate(n,eta_list,H,dt,surf):
        surf[0].remove()
        surf[0] = ax.plot_surface(X/1000.,Y/1000.,H+eta_list[n],cmap=cm.coolwarm,vmin=H-0.005*H,vmax=H+0.005*H);
        ax.set_title('Surface height $h$ at time = {:.2f} hours'.format(n*sample_interval*dt/3600.),fontsize=18)  
        return surf

    fig = plt.figure(figsize=(16,8));
    ax = fig.gca(projection='3d');
    ax.set_zlim(H-0.005*H,H-0.005*H);
    surf = [ax.plot_surface(X/1000.,Y/1000.,H+eta_list[int(len(eta_list)/2)],cmap=cm.coolwarm,vmin=H-0.005*H,vmax=H+0.005*H)];
    ax.set_xlabel('$x$ [km]',fontsize=14);
    ax.set_ylabel('$y$ [km]',fontsize=14);
    fig.colorbar(surf[0], shrink=0.5, aspect=5);

    anim = animation.FuncAnimation(fig,animate,frames=range(0,len(eta_list),interval),fargs=(eta_list,H,dt,surf))
    anim.save("{}.gif".format(fileName),writer='imagemagick',fps=20)